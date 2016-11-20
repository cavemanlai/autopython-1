#! python3
# phoneAndEmail.py - Finds phone number and email addresses on the clipboard

import pyperclip
import re

phoneRegex = re.compile(r'''(   #group(1)=group(0)
(\d{3}|\(\d{3}\))?  # area code group(2)
(\s|-|\.)?          # separator group(3)
(\d{3})             # first 3 digits group(4)
(\s|-|\.)           # separator group(5)
(\d{4})             # last 4 digits group(6)
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension group(7(8)(9))
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phon num or email addresses found')