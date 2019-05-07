#Omar De La Torre

#4/20/2019

def add_fruit(inventory, fruit, quantity=0):
    if 'strawberries' not in new_inventory:
       inventory [fruit] = quantity
    else:
       inventory [fruit] += quantity 
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
if 'strawberries' in new_inventory:
    print("Yes. 'Strawberries' is a key")
print(new_inventory)
add_fruit(new_inventory,'strawberries',25)
print(new_inventory)


