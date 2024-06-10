#An Armstrong number equals the sum of the cubes of its digits.
n = int(input("Enter a number to check whether it is an Armstrong number: "))

sum = 0
temp = n
orderLengthOfNumber = len(str(n))
isOrNot = " not "

while 0 != temp:
    digit = temp%10
    sum += digit**orderLengthOfNumber
    temp //= 10
if sum == n:
    isOrNot = " "

print("The number",n,"is"+isOrNot+"an Armstrong number.")