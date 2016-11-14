#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()
textlist = text.split('\n')
for i in range(len(textlist)):
    textlist[i] = '* ' + textlist[i]
text = '\n'.join(textlist)
pyperclip.copy(text)