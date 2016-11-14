#! python3
#pw.py - An insecure password locker program.

PASSWORDS = {'email': '111111',
             'blog': '222222',
             'luggage': '333333'}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit('goodbye')

account = sys.argv[1]  #first commond line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There is no account named' + account)