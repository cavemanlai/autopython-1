inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(dict):
    print('Inventory:')
    count = 0
    for k, v in dict.items():
        print(v, k)
        count = count + v
    print('total:',count)
displayInventory(inventory)