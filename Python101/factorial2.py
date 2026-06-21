def factorial(num):
    if "int" not in str(type(num)):
        return None
    if num == 0:
        return 1
    elif num > 0:
        return int(num) * factorial(num-1)
    return None