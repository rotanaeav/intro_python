import cowsay
cowsay.dragon("Hello, World!")

name = "robizna"
age = 18

def func():
    name = "robizno"
    print("local var: ", name)

func()
print("global name: ", name ,)
print("age : ", age)

# loop
land = "Python"
for x in "Python":
    print (x)

# condiction
text = "Khmer is Khmer not Vietnam"
print ("Kh" in text)

#slicing
# print(len(text))
# print(text[:8])
# print(text[11:])

print(text.upper)
print(text.lower)
print(text.strip)

you = "koko"
me = "jenny"
print("My name's "+ me + "" + "Your name's " + you)
