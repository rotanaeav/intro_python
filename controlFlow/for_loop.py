# for loop
# for .. in range( start,stop,step)
for i in range(1,10):
    print(i)
for j in range(0,10,2): #step can negative if we range from big to small (10,0,-2)
    print(j)

# while loop
k = 5
while k > 0:
    print("k is : " ,k)
    k-=1

print("Menu")
print("1. Create Product")
print("2. Delete Product")
print("3. Edit Product")
print("4. Exit")
opt = int(input("Enter your option: "))
while True:
    if opt == 1:
        print("Creating Product")
        break
    elif opt == 2:
        print("Deleting Product")
        break
    elif opt == 3:
        print("Editing Product")
        break
    elif opt == 4:
        print("Exit")
        break
    else :
        print("Invalid option")
        break
for i in range(5):
    if i==3:
        continue
    print(i)