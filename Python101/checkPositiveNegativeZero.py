num = int(input("Enter a number to check for being positive/negative/zero: "))
# handle exception for non-numeric string and empty string

if num>0:
    print("The number",num,"is positive.")
elif num<0:
    print("The number",num,"is negative.")
else:
    print("The number",num,"is zero.")