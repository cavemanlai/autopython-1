#! python3
# searchAllText.py - open all files of an directory and search a line by regex
# Boston

import re
import os

allFiles = os.listdir('C:\\Users\\daize\\Desktop\\pythonTEST\\autopython\\act8\\quizEX')
lineRegex = re.compile(r'[AB]\w{1,5}[on]')
for file in allFiles:
    catFile = open('C:\\Users\\daize\\Desktop\\pythonTEST\\autopython\\act8\\quizEX\\%s' % file)
    fileContent = catFile.read()
    print(lineRegex.findall(fileContent))
    catFile.close()