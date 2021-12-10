#! /usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ELApp")
sys.path.insert(0,"/var/www/ELApp")

from ELApp import app as application
application.secret_key = 'temp'
