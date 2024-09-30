# Python code​​​​​​‌​‌​‌‌‌‌‌​‌‌​‌‌​​‌‌‌​​​‌​ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    # Your code goes here.
    primes=[]
    for number in range(2,num):
        for factor in primes if factor < int(number **0.5)+1 :
            if number % factor !=0:
                print(f'{number} is prime')
                primes.append(number)
    return primes



# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.
num = 100
result = Answer.allPrimesUpTo(num)
