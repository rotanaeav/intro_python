# import subprocess
# subprocess.run("clear", shell=True)

java_score = float(input("Enter Java Score: "))
devops_score = float(input("Enter Devops Score: "))
python_score = float(input("Enter Python Score: "))
total = java_score + devops_score + python_score
average = total/3
#elif and if (elif = else if)
if average >= 90:
    print("You got Grade A")
elif average >= 80:
    print("You got Grade B")
elif average >= 70:
    print("You got Grade C")
elif average >= 60:
    print("You got Grade D")
elif average >= 50:
    print("You got Grade E")
else:
    print("You got Grade F")

# Ternary Operator
a=10
b=20
print("a") if a>b else print("=") if a==b else print("b")
