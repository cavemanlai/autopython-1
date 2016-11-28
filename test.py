import re
import os
import urllib.request, urllib.parse

url = 'http://192.168.10.61/zabbix/index.php'
# url = 'http://192.168.10.61/zabbix/tr_status.php?filter_set=1&groupid=2&hostid=0&show_triggers=1&sid=254050934e847cac'
value = {'username': 'Admin', 'password': 'fairlink'}
data = urllib.parse.urlencode(value).encode('utf-8')
req = urllib.request.Request(url, data)
# print(req)
# response = urllib.request.urlopen(req).read()
response = urllib.request.urlopen(req)
# print(response)
# print(response.read())
# print(response.getcode())
print(response.getallheaders())
# urllib.request.build_opener()
# http://192.168.10.61/zabbix/chart2.php?graphid=897&period=3600&stime=20161128130648&updateProfile=1&profileIdx=web.screens&profileIdx2=897&sid=254050934e847cac&width=1776&screenid=&curtime=1480319746979