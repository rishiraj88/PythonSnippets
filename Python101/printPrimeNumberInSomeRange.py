lower = int(input("Enter the lower number (inclusive) for range: "))
higher = int(input("Enter the higher number (inclusive) for range: "))

if lower > higher:
    lower,higher = higher,lower

outputStatus = ""
list = []
for num in range(lower,higher+1):
    if num>1:
        status = "prime"
        for i in range(2, int(num ** 0.5) + 1):
            if num%i == 0:
                status = "not prime"
                break
        if status == "prime":
            outputStatus = "Prime numbers in the range of "+str(lower)+" to "+str(higher)+" are: "
            list.append(num)

if "" != outputStatus:
    print("Prime numbers in the range of",lower,"to",higher,"are: ")
    print(list)
else:
    print("No prime numbers found between",lower,"to",str(higher)+".")