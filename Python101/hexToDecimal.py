hexNums = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,    
    'F':15,
}

def hexToDec(hexNumber):
    for ch in hexNumber:
        if ch not in hexNums:
            return None
    
    decNumber = 0
    power = len(hexNumber) - 1

    for ch in hexNumber:
        decNumber += hexNums[ch] * (16**power)
        power = power - 1
    
    return decNumber