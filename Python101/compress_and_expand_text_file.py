# Python code​​​​​​‌​‌‌‌‌​‌‌​​​​​​​‌‌​​‌‌​‌‌ below
import json
import os

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    # Your code goes here.
    pass

def decodeFile(filename):
    # Your code also goes here.
    pass
    


################
original_filesize = os.path.getsize("./new 1.txt")
print(f'Original file size: {original_filesize}')
encodedFile = encodeFile('new 1.txt', 'new 1_encoded.txt')

new_filesize = os.path.getsize("./new 1_encoded.txt")
print(f'New file size: {new_filesize}')
decodedContent = encodedFile.decodeFile('new 1_encoded.txt')
print(decodedContent)