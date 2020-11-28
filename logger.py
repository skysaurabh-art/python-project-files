import logging

""" This module creates LOG file to keep the log of every run"""

logging.basicConfig(filename='test1_LOGS.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)