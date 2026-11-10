user_response = {
    "id": 101,
    "username": "admin",
    "country": "Cambodia"
}
# we can use  get("key") to get specific key
print(user_response.get("id"))
# just add , to key for show if none of key
print(user_response.get("koko", "No Key Provided"))
# we want to directly access to key ; but if it none of key it will error
print(user_response["username"])
# to get all keys :
print(user_response.keys())

# use with loop for condiction:

# correct_key= {"email":"","username":"admin","password":""}
# to get all values :
revenue={"Mon":100,
"Tue":101,
"Wed":102,
"Thur":103,
"Fri":104,
"Sat":105,
"Sun":106}
print(sum(revenue.values()))

# using loop :
menu={
    "Coffee":1,
    "Tea":2,
    "Rice":3, }
for key, value in menu.items():
    print(key, value)

# change :
change= {
    "username":"koko",
    "theme": "dark"
}

# profile = user_response.update(change)
# print(profile)

# copy :
org_setting = {
    "volume":50,
    "brightness":100
}
backup_setting = org_setting.copy()
org_setting["volume"]= 77
print("ORG: ",org_setting)
print("BU: ",backup_setting)

# setdefault if no key (no key not null or empty)
user_setting ={
    "theme":"dark",
    "volume":50,
    "brightness":100
}
user_setting.setdefault("theme","green")
print(user_setting)

