from import_libs import *

""" This module creates LOG file to keep the log of every run"""

logging.basicConfig(filename='my_LOGS.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)