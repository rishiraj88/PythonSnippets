print("Even or Odd Number")
num = int(input("Enter a number to check: "))
# to exclude 0 and negative numbers?
if num%2 == 0:
    print("The number",num,"is even.")
else:
    print("The number",num,"is odd.")