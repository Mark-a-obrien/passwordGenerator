import random
import pyperclip

special = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
lowerCaseAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCaseAlphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 

totalChar = special + lowerCaseAlphabet + upperCaseAlphabet + numbers
totalCharLength = 94

totalAlphabet = lowerCaseAlphabet + upperCaseAlphabet

def getRandomNum(len):
    return random.randint(0, len-1)

def addCharacters(length, listType): 
    password = ""
    for i in range(length):
        password += listType[getRandomNum(len(listType))]

    return password

def randomizeOrder(password):
    tempPassword = ""

    password = list(password)

    for i in range(len(password)):
        index = getRandomNum(len(password))
        tempPassword += password[index] # Adds random char to tempPassword
        password.pop(index) # Removes char from password

    return "".join(tempPassword)

def addAllCharacters(length, numSpecial, numNumbers, numUppercase): 
    nonStandardChars = numSpecial + numNumbers + numUppercase

    # Adds lowercase characters
    password = addCharacters(length-(nonStandardChars), lowerCaseAlphabet)

    # Adds non standard cahracters
    password += addCharacters(numSpecial, special)
    password += addCharacters(numNumbers, numbers)
    password += addCharacters(numUppercase, upperCaseAlphabet)

    return password

def genPassword(length=8, numSpecial=1, numNumbers=1, numUppercase=1): 
    password = addAllCharacters(length, numSpecial, numNumbers, numUppercase)

    print(password)

    password = randomizeOrder(password)

    return password


password = genPassword(16, 3, 4, 1)
pyperclip.copy(password) # Copies to clipboard
print(password)

stopTheWindowFromClosing = input("Press any button to close")

