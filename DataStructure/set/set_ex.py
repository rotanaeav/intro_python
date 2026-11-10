# back up diff item
# set up
yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}

# 2
new_file = today.difference(yesterday)
old_file = yesterday.difference(today)
print("New File Today : ",new_file)
print("Removed File : ",old_file)

#3
same_file = today.intersection(yesterday)
print("Same File : ",same_file)

#4
diff_file = today.symmetric_difference(yesterday)
print("All Different Files : ",diff_file)

#5
all_files = today.union(yesterday)
# print("All Files : ",all_files)
print("All Files : ",sorted(all_files))