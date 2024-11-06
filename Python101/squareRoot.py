import math

# method 1 (using math module)
num = 49
sqrt = math.sqrt(num)
print (f"The square root of {num} is {sqrt}")

# method 2 (using math module)
num = 64
sqrt = math.pow(num,0.5)
print (f"The square root of {num} is {sqrt}")

# method 3 (using exponentiation operator **)
num = float(input("Enter a number to get its square root: "))

sqrt = num**(0.5) # sqrt = num**(1/2)
print (f"The square root of the input number {num} is {sqrt}")