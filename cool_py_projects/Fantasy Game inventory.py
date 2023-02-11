#! python3
Inven_tory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_Inventory(inventory):
    print('Inventory:')
    Total_item = 0
    for i,m in inventory.items():
        print('{m} {i}'.format(m = m, i = i))
        Total_item += m
    print('Total number of items: {j}'.format(j = Total_item))
def addToinventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToinventory(Inven_tory, dragonLoot)

display_Inventory(Inven_tory)
input()


