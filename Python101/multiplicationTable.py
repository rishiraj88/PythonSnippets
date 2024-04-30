n = int(input("Enter a number to view its multiplication table: "))

# method 1 (using for range() loop)
for i in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    print(n,"x",i,"is", n*i)

# method 2 (using while loop)
i = 1
while i<=10:
    print(n,"x",i,"=", n*i)
    i += 1;
