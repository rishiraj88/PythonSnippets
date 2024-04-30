# method 1 (using the third variable)
print("Swapping two numbers using method 1 (using the third variable)")
x = 10
y = 20
print("The numbers are: ",x," and ",y)

print("Swapping the numbers...")
temp = x
x = y
y = temp
print("Now the numbers are: ",x," and ",y)

# ===

# method 2 (without the third variable)
print("\nSwapping two numbers using method 2 (without the third variable)")
x = 11
y = 22
print("The number are: ",x," and ",y)

print("Swapping the numbers...")
x,y = y,x
print("Now the numbers are: ",x," and ",y)

