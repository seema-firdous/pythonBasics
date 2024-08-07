#Display three string “Name”, “Is”, “James” as “Name**Is**James”
print('My', 'Name', 'Is', 'James', sep='**')

#Convert Decimal number to octal using print() output formatting
num = 8
print('%o' % num)

#Display float number with 2 decimal places using print()
num = 458.541315
print('%.2f' % num)

#Get Multiple inputs From a User in One Line
name, age, marks = input("Enter your Name, Age, Percentage separated by space ").split()
print("\n")
print("User Details: ", name, age, marks)

print('FirstName - {0}, LastName - {1}'.format('Ault', 'Kelly'))


#Display Output Number in Various Format
number = int(input("Enter number "))

print("\n")
# 'd' is for integer number formatting
print("The number is:{:d}".format(number))

# 'o' is for octal number formatting, binary and hexadecimal format
print('Output number in octal format : {0:o}'.format(number))

# 'b' is for binary number formatting
print('Output number in binary format: {0:b}'.format(number))

# 'x' is for hexadecimal format
print('Output number in hexadecimal format: {0:x}'.format(number))

# 'X' is for hexadecimal format
print('Output number in HEXADECIMAL: {0:X}'.format(number))

#Display Numbers as a float type
number = float(input("Enter float Number "))

print("\n")
# 'f' is for float number arguments
print("Output Number in The float type :{:f}".format(number))

# padding for float numbers
print('padding for output float number{:5.2f}'.format(number))

# 'e' is for Exponent notation
print('Output Exponent notation{:e}'.format(number))

# 'E' is for Exponent notation in UPPER CASE
print('Output Exponent notation{:E}'.format(number))

#Output String Alignment
text = input("Enter String ")

print("\n")
print("Left justification", text.ljust(16, "*"))
print("Right justification", text.rjust(16, "*"))
print("Center justification", text.center(16, "*"))
