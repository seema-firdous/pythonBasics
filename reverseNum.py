#Write a Program to extract each digit from an integer in the reverse order.
def reverse(num):
    print("Entered number is: ",num)
    print("Reverse number is: ")
    while num > 0:
        last_dig = num % 10
        print(last_dig, end=" ")
        num = num // 10
        
num=int(input())
reverse(num)
