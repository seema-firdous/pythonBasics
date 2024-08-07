#Palindrome number
def palindrome(num):
    print("Original Number: ",num)
    original_num = num
    reverse_num=0
    while num > 0:
        last_digit = num % 10
        reverse_num = (reverse_num * 10) + last_digit
        num = num // 10
        
    print ("Reverse Number: ", reverse_num)
    if original_num == reverse_num:
        print("This is a palindrome")
    else:
        print("Not a palindrome")
      
value = int(input())
palindrome(value)
