#!/usr/bin/env python

import os
import sys
import redis
import bottle
import logging
import xmlrpclib

from bottle import route
from config import cfget

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

foxrate = xmlrpclib.ServerProxy("http://foxrate.org/rpc/").foxrate

rdb = redis.Redis(host=cfget('/redis.*/hostname', 'localhost'),
                  port=cfget('/redis.*/port', 6379),
                  password=cfget('/redis.*/password'))

def currencies(db=[]):
    if not db:
        with open("currencies.dat", 'r') as f:
            for line in f.readlines():
                symbol, title = line.strip().split("\t", 1)
                db.append((symbol, title))
    return db

def get_upstream_rate(src, dst):
    result = foxrate.currencyConvert(src, dst, 1.0)
    if result['flerror'] != 0:
        raise Exception(result['message'])
    return str(result['amount'])

@route('/')
def home():
    return bottle.template('home', currencies=currencies())

@route('/rate/:src#[A-Z]{3}#/:dst#[A-Z]{3}#')
def get_rate(src, dst):
    for i in range(3):
        try:
            rate = rdb.get(src + dst)
            if rate is None:
                rate = get_upstream_rate(src, dst)
                rdb.setex(src + dst, rate, 3*60*60)
            return '' if rate == '' else str(float(rate))
        except:
            logging.exception("can't get rate %s:%s (%s)" % (src, dst, 
                                                             repr(rate)))
            rdb.delete(src + dst)
    raise

@route('/static/:filename')
def serve_static(filename):
    return bottle.static_file(filename, root=STATIC_ROOT)

application = bottle.app()
application.catchall = False

if os.getenv('SELFHOST', False):
    bottle.run(application)

