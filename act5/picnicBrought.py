allGuests = {'Alice': {'apples': 5, 'pretzeles': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(dict, item):
    numBrought = 0
    for k, v in dict.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Apple:'+str(totalBrought(allGuests, 'apples')))
print('Pretzeles:'+str(totalBrought(allGuests, 'pretzeles')))
print('Ham Sandwiches:'+str(totalBrought(allGuests, 'ham sandwiches')))
print('Cups:'+str(totalBrought(allGuests, 'cups')))
print('Apple Pies:'+str(totalBrought(allGuests, 'apple pies')))
print('Cake:'+str(totalBrought(allGuests, 'cake')))

