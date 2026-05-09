# LAB 3
# CALCULATING FEDERAL TAX BASED ON THE VALUES OF ANNUAL GROSS INCOME 

# STEP 1 -- WEEKLY GROSS PAY
hours_worked = float(input("Enter hours worked per week: "))
hourly_rate = float(input("Enter hourly rate: "))

weekly_gross_pay = hours_worked * hourly_rate #calculate weekly gross pay
print("Weekly gross pay:", weekly_gross_pay)

# STEP 2 -- ANNUAL GROSS PAY

#There are 52 weeks in a year
annual_gross_pay = weekly_gross_pay * 52
print("Anual gross pay:", annual_gross_pay)

# STEP 3 -- TAX INPUTS
filling_status = input("Enter filing status (single or joint):").lower ()

# STEP 4 -- SIMPLE TAX RULES (example logic)
# Determine tax rate
if filling_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filling_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00 
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Tax calculations
tax_withheld = weekly_gross_pay * tax_rate
net_pay = weekly_gross_pay - tax_withheld

# Output
print("You worked", hours_worked, "hours this period.")
print("Because you earn $", hourly_rate, "per hour, your gross weekly pay is $", weekly_gross_pay)
print("Your filling status is", filling_status)
print("Your tax withholding for the week is $", tax_withheld)
print("Your net pay is $", net_pay)