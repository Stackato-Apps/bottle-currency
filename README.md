# Currency Converter

## Purpose

Currency Converter is a web app for converting currencies. 

## Technology Stack

 * ActivePython - http://www.activestate.com/activepython
 * Bottle web framework - http://bottlepy.org/
 * Redis NoSQL database - http://redis.io/

The app uses Foxrate XML-RPC API to obtain actual currency
exchange rates. The data is retained in the local Redis 
database for 3 hours.

## Usage

### Deploy on Stackato

    $ git clone git://github.com/Stackato-Apps/bottle-currency.git
    $ cd bottle-currency
    $ stackato push -n

Then open application in a browser.

    $ stackato open

### Without Stackato

It is possible to run the app without Stackato, if necessary.

 1. Install and start Redis database, see http://redis.io for details

 1. Install dependencies:

    $ pypm install -r requirements.txt
 
 2. Run the app:

    $ SELFHOST=1 python ./wsgi.py
    
Then open http://127.0.0.1 in a browser.

## Using New Relic

Before you deploy your application, modify stackato.yml and insert your New Relic license key.
