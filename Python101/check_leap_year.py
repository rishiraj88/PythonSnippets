print("Leap or Non-leap Year")
year = int(input("Enter a year number to check: "))
# handle invalid inputs like negative or zero year number, non-numeric strings input

if 0 >=year:
    print("Invalid input!")

status = "non-leap"
if year%400 == 0:
    status = "leap"
elif year%100 == 0:
    status = "non-leap"
elif year%4 == 0:
    status = "leap"
print("The year",year, "is a",status,"year.")
