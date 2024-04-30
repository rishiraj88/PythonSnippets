num = int(input("How many terms of Fibonacci series to print: "))

a=0
b=1
if num == 1:
    print(a)
elif num > 2:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(1,num-1):
        c = a+b
        print(c,end=" ")
        a=b
        b=c


