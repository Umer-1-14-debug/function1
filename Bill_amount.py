def bill(bill01):
    tip_percentage=bill01*(tip/100)
    total_bill=bill01+tip_percentage
    print("Your total bill is ",total_bill)
tip=float(input("Enter the percentage of the tip "))
bill(1000)