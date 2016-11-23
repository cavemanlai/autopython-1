#! python3

wordFile = open('C:\\Users\\daize\\Desktop\\pythonTEST\\autopython\\act8\\crazyword.txt')
newFile = open('C:\\Users\\daize\\Desktop\\pythonTEST\\autopython\\act8\\crazywordNew.txt', 'w')
# catch = []
catch = wordFile.read().split(' ')
for w in catch:
    if w == 'ADJECTIVE':
        newWord = input('Enter an adjective:\n')
        newFile.write('%s ' % newWord)
    elif w == 'NOUN':
        newWord = input('Enter an noun:\n')
        newFile.write('%s ' % newWord)
    elif w == 'VERB':
        newWord = input('Enter an verb:\n')
        newFile.write('%s ' % newWord)
    else:
        newFile.write('%s ' % w)
wordFile.close()
newFile.close()