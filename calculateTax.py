#Calculate income tax for the given income by adhering to the rules below
"""Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20"""

def calculate_tax(income):
    tax_amount = 0
    if income <= 10000 :
        tax_amount=0
    elif income <= 20000 :
        tax_amount = (income - 10000) * 0.1
    else:
        tax_amount = (10000 * 0.1) + (income - 20000) * 0.2
        
    return tax_amount

income = int(input())
print("Tax to be paid for income ",income," is : ", calculate_tax(income))
        
