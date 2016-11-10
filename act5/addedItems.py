#列表与字典合并

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(dict):
    print('Inventory:')
    count = 0
    for k, v in dict.items():
        print(v, k)
        count = count + v
    return count

def addToInventory(inventoryDict, addedItems):
    for i in addedItems:
        inventoryDict[i] = inventoryDict.setdefault(i, 0) + 1
    displayInventory(inventoryDict)

addToInventory(inventory, dragonLoot)
