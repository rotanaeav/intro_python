# tuple create :
fruits = ("grap", "banana", "durian")
print(fruits)

# to change items or value of tuple we need to convert it to list first
new_fruits = list(fruits)
print(new_fruits)
new_fruits[0] = "banana"
print(new_fruits)
fruits = tuple(new_fruits)
print(fruits)

#find index :
print(fruits.index("banana"))