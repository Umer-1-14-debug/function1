try:
    age=int(input("Enter a your age"))
    if age<=0:
        print(ValueError)
    else:
        print("You are eligible")
except ValueError:
    print("Age cannot be negative or zero")