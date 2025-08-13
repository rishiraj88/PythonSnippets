print("To check which integers in a both-limits-inclusive range are Armstrong numbers")
low =int(input("Enter the lower limit of the range: "))
high=int(input("Enter the upper limit: "))

#assuming both numbers to be in a common order. Order means the count of digits in a given number
def armstrongNumsInRange(low,high):
    armstrongNumbers = []
    for n in range(low, high + 1):
        sum = 0
        orderLengthOfNumber = len(str(n))
        temp = n
        while 0 != temp:
            digit = temp % 10
            sum += digit ** orderLengthOfNumber
            temp //= 10
        if n == sum:
            armstrongNumbers.append(n)
    print(f"\nArmstrong numbers in the range [{low},{high}] are: {armstrongNumbers}")
    return armstrongNumbers

if __name__=='__main__':
    armstrongNumsInRange(111,999)