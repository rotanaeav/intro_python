
# arithmatic : + , - ,* , / , % , ** , //
x = 20
y = 30
result = x + y
print(result)
#even is ku

if x%2 == 0:
    print("x is even")
else:
    print("x is odd")

#Assignment
x = 20
x = x +1
x += 2 #shorthand

#Comparison operator and Logical (and , or , not)
age = input("Enter your age: ")
nationality = input("Enter your nationality: ")
if int(age) >= 18 and nationality == "khmer":
    print("You are eligible for election !")
else:
    print("You are not eligible for election !")

#Identity (is , is not )
z = [1,2,3]
m = [1,2,3]
print(z is m)
print(id(z))

#Membership (in , not in)
print(z in m)
