#! python3
# backupToZip.py - copies an entire folder and its contents into a ZIP file whose filename increments

import os
import zipfile

# os.chdir('C:\\Users\\daize\\Desktop\\pythontest\\autopython\\act9')
def backupToZip(folder):
    # backup the entire contents of 'folder' into a ZIP file.

    folder = os.path.abspath(folder)    # make sure 'folder' is absolut

    # figure out the filename this code should use based on what files already exist
    num = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zipFilename):
            break
        num = num + 1

    # create the ZIP file
    print('Creating %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % foldername)
        # adding the current folder to the ZIP file.
        backupZip.write(foldername)
    # add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # do not backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

backupToZip('data_bak')