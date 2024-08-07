# list to store multi line input
# press enter two times to exit
data = []
print("Tell me about yourself")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break
finalText = ' '.join(data)
finalText2 = " " + str(data)
print("Final text input")
print(finalText)
print("***************")
print("Final text input another way")
print(finalText2)
