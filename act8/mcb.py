#! python3
# mcb.pyw - muti copy & paste from clipboard
# Usage: py.exe mcb.py save <keyword> - save clipboard to keyword
# py.exe mcb.py <keyword> - loads keyword to clipboard
# py.exe mcb.py list - loads all keywords to clipboard
# py.exe mcb.py delete <keyword> - delete keyword

import pyperclip
import sys
import shelve

macShelf = shelve.open('C:\\Users\\daize\\Desktop\\pythontest\\autopython\\act8\\mcb\\mcb')
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        macShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del macShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1] in macShelf:
        pyperclip.copy(macShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'list':
        print(str(list(macShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        macShelf.clear()

macShelf.close()