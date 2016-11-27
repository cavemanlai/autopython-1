#! python3
# changeNameNum.py - change the number of the filename

import shutil
import os
import re

nameRegex = re.compile(r'^(spam)(\d{3})\.txt$')

def changenamenub(folder):
    lst = []
    for file in os.listdir(os.path.abspath(folder)):
        mo = nameRegex.search(file)
        if mo == None:
            continue
        lst.append(mo.group())
    lst = sorted(lst)
    print(lst)
    num = 1
    for f in lst:
        mon = nameRegex.search(f).group(2)
        mo1 = nameRegex.search(f).group(1)
        path = os.path.abspath(folder)
        f = path + '\\' + f
        if str(mon) == str(num).rjust(3, '0'):
            num += 1
        elif str(mon) != str(num).rjust(3, '0'):
            newMon = str(num).rjust(3, '0')
            newFile = os.path.dirname(f) + '\\' + mo1 + newMon + '.txt'
            shutil.move(f, newFile)
            num += 1

changenamenub('data_bak_new')