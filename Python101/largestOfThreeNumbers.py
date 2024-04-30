num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1>num2:
    if num1>num3:
        print("The first number",num1,"is the largest.")
    else:
        print("The third number",num3,"is the largest.")
elif num2>num3:
    print("The second number",num2,"is the largest.")
else:
    print("The third number",num3,"is the largest.")