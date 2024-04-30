#An Armstrong number equals the sum of the cubes of its digits.
n = int(input("Enter a number to check for being an Armstrong number: "))

sum = 0
order = len(str(n))
temp = n

isOrNot = " not "

while 0 != temp:
    digit = temp%10
    cube = digit**order
    sum += cube
    temp //= 10

if sum == n:
    isOrNot = " "

print("The entered number",n,"is"+isOrNot+"an Armstrong number.")