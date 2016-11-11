def printPicnic(itemDict, leftWidth, rightWidth):
    print('Picnic Item'.center(leftWidth+rightWidth,'-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples:': 12, 'cups': 4, 'cookies:': 8000}
printPicnic(picnicItems, 15, 5)
printPicnic(picnicItems, 20, 6)