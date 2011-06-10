# Currency Converter

## Purpose

Currency Converter is a web app for converting currencies. 

## Technology Stack

 * ActivePython - http://www.activestate.com/activepython
 * Bottle web framework - http://bottlepy.org/
 * Redis NoSQL database - http://redis.io/

The app uses Foxrate XML-RPC API to obtain actual currency
exchange rates.

## Usage

### Using Stackato platform

Push the app to the Stackato server:

    $ stackato push converter
    Would you like to deploy from the current directory ?  [Yn]:
    Application Deployed URL: 'converter.stackato.local'? 
    Detected a Python WSGI Application, is this correct ?  [Yn]:
    Memory Reservation ?  (64M, 128M, 256M, 512M, 1G, or 2G): 
    Creating Application: OK
    Would you like to bind any services to 'converter' ?  [yN]: y
    Would you like to use an existing provisioned service ?  [yN]: n
    The following system services are available
    1. mongodb
    2. mysql  
    3. redis  
    Please select one you wish to provision: 3
    Specify the name of the service [redis-xxxx]: 
    Creating Service: OK
    Binding Service: OK
    Uploading Application:
      Checking for available resources: OK
      Processing resources: 'OK
      Packing application: OK
      Uploading (0K): 51% OK
    Push Status: OK
    Staging Application: OK
    Starting Application: OK

Then open http://converter.stackato.local in a browser.

### Without Stackato

It is possible to run the app without Stackato, if necessary.

 1. Install and start Redis database, see http://redis.io for details

 1. Install dependencies:
    $ pypm install -r requirements.txt
 
 2. Run the app:
    $ SELFHOST=1 python ./wsgi.py
    
Then open http://127.0.0.1 in a browser.


