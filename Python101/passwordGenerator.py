# to generate a random password string, given the desired length of the to-be-generated password
# author rishiraj
# on 20221213

import random

passLen = int(input("Enter the password length: "))
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()-_+={}[]|\;:\"<>,./?" # password seed

# to increase the length of seed when required
charsetLen = len(s);
print(charsetLen)
if charsetLen < passLen:
    s = s*(passLen//charsetLen +1)
    print(s)
charsetLen = len(s);
print(charsetLen)

# generating the password string
password = "".join(random.sample(s,passLen))
print(password)