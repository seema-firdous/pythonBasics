#Remove first n characters from a string
word=input()
noOfChar = int(input())
print("String entered is : ",word)
print("String after first ",noOfChar, " characters removed is : ",word[noOfChar:])
