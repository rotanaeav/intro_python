#1. Create :
inventory = {
    "milk": 5,
    "coffee": 0,
    "cake": 20,
}
#2. Get
print("Coca: ",inventory.get('coca'))

#3. update :
update={
    "milk": 10,
    "rose": 20,
    "egg": 5,
}
inventory.update(update)
# print(inventory)

#4. print items:
for k, v in inventory.items():
    print("Name: ",k, ", Qty:",v)

#5. remove with pop()
# inventory.pop('milk')
for k, v in list(inventory.items()):
    if v == 0:
        inventory.pop(k)
print(inventory)

#6. setdefault
inventory.setdefault('matcha', 10)
# print(inventory)

#7. use sum() and value()
print("Total Qty:",sum(inventory.values()))

# 8. copy() :
new_inv=inventory.copy()
inventory.clear()
print("Backup : ", new_inv)
print("Original : ",inventory)

