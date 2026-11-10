# Declare List :
fruits = ["apple", "banana", "cherry","banana"]
print(fruits[0])
# use append() to add to last index
# use .insert(index) to add to specific index
fruits.insert(1, "rose")
print(fruits)
# use pop() for to remove an item by index
# use del_ my_list[index]
# or use remove() to delete by value
# note : with pop() we can store data and  use the remove item but with del you can't .

fruits.remove("banana") # delete only 1 however it has duplicate
print(fruits)
for i in fruits:
    # if fruits.count("banana") >= 2:
    #     print(fruits)
    if i == "banana":
        fruits.remove("banana")
print(fruits)

if "rose" in fruits:
    print("mango is found !!!")