# method 1 (using math module)
import math

num = 49

# style a
sqrt = math.sqrt(num)
print ("The square root of the number is",sqrt)

# style b
num = 64
sqrt = math.pow(num,0.5)
print ("The square root of the number is",sqrt)

# ===

# method 2 (using exponentiation operator **)
num = float(input("Enter a number to get its square root: "))

sqrt = num**(0.5) # sqrt = num**(1/2)
print ("The square root of the number is",sqrt)