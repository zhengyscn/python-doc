

# import ConfigParser
import os
from six.moves import configparser

'''
https://docs.python.org/3/library/configparser.html
'''

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'my.cnf')


cfg = configparser.ConfigParser()
cfg.read(CONFIG_FILE)

print(cfg.get("mysqld", "datadir"))