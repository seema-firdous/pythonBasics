#Create a new list from two list using the following condition
"""Given two list of numbers, write a program to create a new list 
such that the new list should contain odd numbers from the first list 
and even numbers from the second list."""

def list_concat(list1, list2):
    result_list=[]
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
            
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
            
    return result_list
    
    
list1 = [10,23,24,26,2, 8, 9, 3, 5]
list2 = [11,23,14,15,16,17,18,19]
res = list_concat(list1, list2)
print(res)
