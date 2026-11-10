#1.1 Create
student = ("Dara",20,"IT","Year 3")
#1.2 Print
print(f"Student_Name: {student[0]} , Major: {student[2]}")
#1.3 total number of items
print("Length of Student : ",len(student))
#1.4 print year using -1
print("Student_Year : ", student[-1])

#2.1 create
courses = ("Python", "Database", "Network", "Web_Development", "Python")
#2.2 count py
print("Count of Python : ", courses.count("Python"))
#2.3 find index of nw
print("Index of Network : ", courses.index("Network"))
#2.4 using for loop
for i in courses:
    print(i)

#3.1 create
registered_courses = ("Python", "Network", "Database")
print(registered_courses)
#3.2 convert to list
courses_list = list(registered_courses)
#3.3 add c_c
courses_list.append("Cloud_Computing")
#3.4 back to tuple
registered_courses = tuple(courses_list)
#3.5 print
print(registered_courses)



