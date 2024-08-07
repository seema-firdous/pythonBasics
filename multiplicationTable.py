#Print multiplication table from 1 to 10
def table(num):
    for i in range(11):
        print(num," x ",i," = " ,num*i)
        
for j in range(1,11):
    print("Table for ", j," : ")
    table(j)
    print("**********************")
