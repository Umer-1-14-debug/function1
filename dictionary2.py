dict1 = {"Pakistan": 92, "India": 91, "Afghanistan": 93}
v = input("Enter the country name for which you want to know the code: ")
if v in dict1:
    print("The country code of", v, "is", dict1[v])
