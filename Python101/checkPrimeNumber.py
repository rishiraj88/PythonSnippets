print("Prime Number Check")
num = int(input("Enter a number to check: "))

status = "prime"
if num <= 1:
    status = "not prime"

for i in range(2,num):
    print("i is",i)
    if 0 == num%i:
        status = "not prime"
        break

print("The number",num,"is",status)