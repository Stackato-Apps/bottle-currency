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

### Deploy on HPE Helion Stackato

    Server side:
    $ kato role add redis # if not present

    Client side:
    $ stackato push -n

Then open application in a browser.

    $ stackato open

### Without HPE Helion Stackato

It is possible to run the app without HPE Helion Stackato, if necessary.

 1. Install and start Redis database, see http://redis.io for details

 1. Install dependencies:

    $ pypm install -r requirements.txt
 
 2. Run the app:

    $ SELFHOST=1 python ./wsgi.py
    
Then open http://127.0.0.1 in a browser.


