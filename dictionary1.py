dict1={1:"umer",2:"umer"}
v=input("Enter the word you want to know the frequency")
count=0
for key in dict1:
    if dict1[key]==v:
        count=count+1
print(v," occures ",count," numbers of times")