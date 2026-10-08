raw_data = "sTUDENT | 2026 | sOk pANha | 007 | 19 | 3.75"
id = raw_data.split(" | ")[0]+"-"+raw_data.split(" | ")[1]
name = raw_data.split(" | ")[2]
age = int(raw_data.split(" | ")[4])
gpa = float(raw_data.split(" | ")[5])
print("=================Student Report===================")
print("Student ID: " + id.upper())
print("Name: " + name.title())
print("Age: " , age) #can use ", " with non string ;
print("GPA: " + str(gpa))

print("ID contain 2026: " + str("2026" in id))
print("Next year age: " + str(age + 1))
print("Double GPA: " + str(gpa*2))

