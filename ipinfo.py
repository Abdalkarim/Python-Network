#!/usr/bin/python
# coding:utf-8
# About of IP address
# Author : Mahmoud Abd Alkarim(@Maakthon)

from urllib2 import urlopen
from json import load

url  = "http://ipinfo.io/json"
res  = urlopen(url)
data = load(res)

ip       = data['ip']
org      = data['org']
city     = data['city']
region   = data['region']
country  = data['country']
location = data['loc']

print('''
_______________________________

|   IP address information    |
_______________________________
|
| IP address   : {0}
| City         : {1}
| Region       : {2}
| Country      : {3}
| Location     : {4}
| Organization : {5}
| 
'''.format(ip,city,region,country,location,org))
