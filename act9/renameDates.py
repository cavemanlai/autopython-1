#! python3
# renameDates.py - renames filenames with American MM-DD-YYYY date format to Eruopean DD-MM-YYYY

import re
import os
import shutil

dateRegex = re.compile(r'''
^(.*?)       #?作用为非贪婪匹配
([01]?\d)-
([0-3]?\d)-
(\d{4})
(.*?)$
''', re.VERBOSE)

os.chdir('C:\\Users\\daize\\Desktop\\pythontest\\autopython\\act9\\date')
# for filename in os.listdir():
#     findDate = dateRegex.findall(filename)
#     print(findDate)
#     day = findDate[0][2]
#     mouth = findDate[0][1]
#     newFile = findDate[0][0] + day + '-' + mouth + '-' + findDate[0][3] + findDate[0][4]
#     shutil.move(filename, newFile)

for filename in os.listdir():
    findDate = dateRegex.search(filename)
    if findDate == None:
        continue
    beforePart = findDate.group(1)
    monthPart = findDate.group(2)
    dayPart = findDate.group(3)
    yearPart = findDate.group(4)
    afterPart = findDate.group(5)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #get the full ,absolute file paths
    absWorkingDir = os.path.abspath('.')
    filename = os.path.join(absWorkingDir, filename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #rename the files
    print('renameing "%s" to "%s"' % (filename, euroFilename))
    # shutil.move(filename, euroFilename)