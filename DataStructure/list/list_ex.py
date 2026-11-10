# I use def cuz teacher already showing us abit -_-
def print_total(_shopping):
    print("[+]Total items : ",len(_shopping))
#1. List Create :
shopping = ["milk", "cake", "coca", "milk", "coffee"]
#2. Print second, last , and length
print(f"The Second: {shopping[1]} , The last: {shopping[-1]} and Total: {len(shopping)}")
#3. add eggs
shopping.append("eggs")
print("Before add bread: ",shopping)
#3. if we add bread the old second will move to third and the length increase
shopping.insert(1, "bread")
print("After: ",shopping)
#4. if we remove milk only one milk will remove
shopping.remove("milk")
print("Removed milk:",shopping)
#5. print number of remain items
print_total(shopping)

#6. loop print items and number of total
for i in shopping:
    print("All By Line : ",i)
print_total(shopping)

#7. remove last and print it
removed = shopping.pop()
print(shopping)
print_total(shopping)

#8. sorted and original view:
sorted_shopping = sorted(shopping)
print("Unsorted : ",shopping)
print("Sorted : ",sorted_shopping)