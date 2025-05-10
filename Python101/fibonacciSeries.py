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
print("\n\n")

#returning Fibo value at n-th index (zero based)
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))