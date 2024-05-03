num = int(input("Enter a number to check for palindrome: "))

n = num
reverse = 0
while n>0:
    digit = n%10
    reverse = digit + 10*reverse
    n = n//10

if num==reverse:
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is not a palindrome.")