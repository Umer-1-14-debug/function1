choice=int(input("Enter 1 if the bill is before due date and enter 2 if the bill is after the due date"))
def bill():
    bill1=10000
    bill1_after=500
    if choice==1:
        print("Your bill is ",bill1)
    elif choice==2:
        print("Your bill is ",bill1+bill1_after)
    else:
        print("You entered a wrong number. Try again")
    