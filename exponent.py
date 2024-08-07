#Write a function called exponent(base, exp) 
#that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    result = base ** exp
    return result
    
base = int(input())
exp = int(input())
print(base," raises to the power of ",exp," is: ",exponent(base, exp))
