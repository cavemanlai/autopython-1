import re
import os
import urllib.request, urllib.parse
import http.cookiejar

# url = 'http://192.168.10.61/zabbix/chart2.php?graphid=897&period=3600&stime=20161128130648&updateProfile=1&profileIdx=web.screens&profileIdx2=897&sid=254050934e847cac&width=1776&screenid=&curtime=1480319746979'
url = 'http://192.168.10.61/zabbix/index.php'
value = {'Username': 'Admin', 'Password': 'fairlink'}
data = urllib.parse.urlencode(value).encode('utf-8')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# req = urllib.request.Request(url, data)
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')]
req = opener.open(url, data)
# req = opener.open('http://192.168.10.61/zabbix/chart2.php?graphid=897&period=3600&width=1776&stime=20161129000000')

# print(req)

# response = urllib.request.urlopen(req).read()
# response = urllib.request.urlopen(req)
# print(response)
print(req.read())
# print(response.getcode())
# urllib.request.build_opener()
# http://192.168.10.61/zabbix/chart2.php?graphid=897&period=3600&stime=20161128130648&updateProfile=1&profileIdx=web.screens&profileIdx2=897&sid=254050934e847cac&width=1776&screenid=&curtime=1480319746979