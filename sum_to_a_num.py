#Calculate the sum of all numbers from 1 to a given number
num = int(input())
sum = 0
for i in range(1,num+1):
    sum = sum + i
    print("Sum of ",i," numbers is: ",sum)
    
print("Total sum is: ",sum)
