dict1={1:{"umer"},2:{"id","251526"},3:{"marks","426"},4:{"marks","426"}}
print(dict1)
dict2={}
for i in dict1.items():
    print(i)
for key,value in dict1.items():
    if value not in dict2.values():
        dict2[key]=value
print(dict2)