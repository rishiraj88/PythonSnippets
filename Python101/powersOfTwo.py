n = int(input("To show what power of 2:"))

result = list(map(lambda x: 2 ** x,range(n+1)))

for i in range(n+1):
    print("2 ^",i, "is:",result[i])