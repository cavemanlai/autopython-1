#! python3
# cpFileToNewFolder.py - move the order type file to another new folder

import shutil
import os
import re

def cpFileToFolder(folder):
    fileRegex = re.compile(r'.*\.txt')
    folder = os.path.abspath(folder)
    os.makedirs('%s_new' % folder)
    newFolder = folder + '_' + 'new'
    for foldernames, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            newfile = fileRegex.search(filename)
            if newfile == None:
                continue
            newfile = newfile.group()
            newfile = os.path.join(foldernames, newfile)
            # print(newfile)
            shutil.copy(newfile, newFolder)


cpFileToFolder('data_bak')