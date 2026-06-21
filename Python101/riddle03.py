# to calculate the square of a number, using triangle numbers

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num)+triangle(num)-num