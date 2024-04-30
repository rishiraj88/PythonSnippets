lower = int(input("Enter the lower number (inclusive) for range: "))
higher = int(input("Enter the higher number (inclusive) for range: "))

for num in range(lower,higher+1):
    if num>1:
        list = []
        status = "prime"
        for i in range(2,num):
            if num%i == 0:
                status = "not prime"
                break
        if status == "prime":
            outputStatus = "Prime numbers in the range of "+str(lower)+" to "+str(higher)+" are: "
            list.append(num)

if "" != outputStatus:
    print("Prime numbers in the range of",lower,"to",higher,"are: ")
    print(list)