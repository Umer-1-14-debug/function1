tuple1=(0,1,0,1,0,1,0,0,0,0,1,1,1)
zero=0
one=0
for x in tuple1:
    if x==0:
        zero+=1
    else:
        one+=1
if zero>one:
    print("Bad weather")
elif zero<one:
    print("Good weather")
else:
    print("The weather is normal")