#! python3
# rmBigFile.py - remove some folder's big file whose size large then 100M

import os

def rmbigfile(folder):
    print(os.path.abspath(folder))
    for folders, subs, files in os.walk(os.path.abspath(folder)):
        for file in files:
            if os.path.getsize(folders + '\\' + file) > 104857600:
                print(folders + '\\' + file + ':' + str(os.path.getsize(folders + '\\' + file)))


rmbigfile('D:\\game\\The Sims 4')