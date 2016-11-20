import re


passwd = re.compile(r'^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$')    #'?='等于号之后的内容需要匹配表达式，不消耗字符串内容
print(passwd.findall('asdfsuuuuuuu7'))
