#Accept a list of 5 float numbers as an input from the user
input_string = input("Enter list of decimal numbers separated by space ")
num_list = input_string.split()
float_list=[]
for i in range(0,len(num_list)):
    float_list.append(float(num_list[i]))
   
print("\nList of decimals entered ... ")    
print(float_list)
print("Type of list ",type(float_list))
