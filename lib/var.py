# -*- coding: utf-8 -*-
# @Time    : 2020-10-15
# @Author  : ohh-haolin
# @FileName: lib/var.py
# @Software: picSpider
# @Blog    ：https://hlz.ink

import configparser

# read conf.ini 
config = configparser.ConfigParser()
config.read('conf.ini', 'UTF-8')

# create global variable
# Data base configuration
DB = dict(config['DB'])
DB['port'] = int(DB['port'])

# get Target
# first -> pixiv, second -> konachan
Target = [int(config['Target']['pixiv']), int(config['Target']['konachan'])]

# get start ID
# first -> mobile, second -> PC
Index = [int(config['ID']['idOfMobile']), int(config['ID']['idOfPC'])]

# get Proxy configuration
if config['Proxy']['enable'] == 'true':
    path = config['Proxy']['address'] + ':' + config['Proxy']['port']
    px = {'http': path, 'https': path}
else:
    px = {}

def saveIndex():
    config.set('ID', 'idOfMobile', str(Index[0]))
    config.set('ID', 'idOfPC', str(Index[1]))
    config.write(open('conf.ini', 'w'))
