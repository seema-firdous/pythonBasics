#Display numbers divisible by 5 from a list
num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print("Numbers divisible by 5: ")
for num in num_list:
    if num  % 5 == 0:
        print(num)
