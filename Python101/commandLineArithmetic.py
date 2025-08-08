import sys

product = 1

del(sys.argv[0])
for argument in sys.argv:
    try:
        number = float(argument)
        product *= number
    except Exception as e:
        print(e)
        print("Only numbers may be accepted, no other types of values")

print(f"The product of the input numbers is: {product}")