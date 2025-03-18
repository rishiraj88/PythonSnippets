print("To check which integers in a both-limits-inclusive range are Armstrong numbers")
low =int(input("Enter lower limit of the range:"))
high=int(input("Enter lower limit:"))

#assuming both numbers to be in a common order
armstrongNumbers = []
for n in range(low,high+1):
    sum=0
    orderLengthOfNumber = len(str(n))
    temp = n
    while 0 != temp:        
        digit = temp % 10
        sum += digit ** orderLengthOfNumber
        temp //= 10
    if n == sum:
        armstrongNumbers.append(n)
print("\nArmstrong numbers in this range are: ",armstrongNumbers)
