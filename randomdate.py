import random
def randomdate():
    date1=int(input("Enter the date"))
    year=int(input("Enter the year"))
    randate=random.randint(1, 12)
    print(date1,randate,year)
randomdate()