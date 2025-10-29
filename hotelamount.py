def bill():
    nights=int(input("Enter how many nights do you want to stay"))
    print("Which city are you from")
    choice=int(input("Nigeria press 1, america press 2, pakistan press3, india press 4"))
    cost=150
    trip=10
    choice1=input("Enter yes if you eant to ga to the trip")
    bill1=0
    if nights<=10:
        bill1=10*cost
        print(bill1)
    elif nights<=20:
        bill1=15*cost
        print(bill1)
    elif nights<=30:
        bill1=20*cost
        print(bill1)
    else:
        bill1=30*cost
        print(bill1)
    if choice==1:
        bill2=2*cost
        print(bill2)
    elif choice==2:
        bill2=3*cost
        print(bill2)
    elif choice==3:
        bill2=4*cost
        print(bill2)
    elif choice==4:
        bill2=4*cost
        print(bill2)
    else:
        print("Try again")
    if choice1=="Yes":
        print(trip)
        totalbill=bill1+bill2+trip
        print("Your total bill is " ,totalbill)
    elif choice=="No":
        print("Your total bill is ",totalbill)
    else:
        print("Wrong try again")