print("To check which integers in a both-extremes-inclusive range are Armstrong numbers")
lo =int(input("Enter smaller number:"))
hi=int(input("Enter bigger number:"))

#assuming both numbers to be in a common order
order=len(str(lo))
armstrongNumbers = []
for n in range(lo,hi+1):
    sum=0
    temp = n
    isOrNot =" not "
    while 0 != temp:
        digit = temp%10
        sum += digit**order
        temp //= 10
    if n == sum:
        isOrNot=" "
        armstrongNumbers.append(n)
    print("The number",n,"is"+isOrNot+"an Armstrong number.")
print("\nArmstrong numbers in this range are:",armstrongNumbers)