num = int(input("Enter a number to get its factorial: "))

# method 1 (using iteration -- for loop) - start
if 0 > num:
    print("Factorial of the number is not possible.")
elif 1 >= num:
    print("Factorial of the number",num,"is:",1)
else:
    factorial = 1
    for i in range(2,num+1):
        factorial *= i
    print("The factorial of",num,"is:",factorial)
# method 1 (using iteration -- for loop) - end

# method 2 (using recursion) - start
# num = int(input("Enter a number to get its factorial: "))

def fact(a):
    if 0 > num:
        return None
    if 0==a or 1==a:
        return 1
    return a*fact(a-1)

num = int(input("Enter a number to get the factorial of: "))
factorial = fact(num)
print("The factorial of",num,"is:",factorial)
# method 2 (using recursion) - end