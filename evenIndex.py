#Print characters from a string that are present at an even index number
word = input()
print("The whole word entered is : ",word)
size = len(word)
for i in range(0,size,2):
    print("index[",i,"]: ",word[i])

#Another way of solving
print("*******************")
word1 = input()
print("Original String:", word1)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word1)
for i in x[0::2]:
    print(i)
