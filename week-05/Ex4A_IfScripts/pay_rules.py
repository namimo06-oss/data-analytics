# LAB 2
# CALCULATING GROSS PAY GIVEN THE VARIABLES pay_rate AND hours_worked

pay_rate = float(input("Enter hourly pay rate: ")) #ask user for hourly rate
hours_worked = float(input("Enter hours worked: ")) #ask for hours worked


# if employee worked more than 40 hrs 
# overtime is pais at 1.5 times normal rate 

if hours_worked > 40:
    regular_pay = 40 * pay_rate #regular hours are limited to 40 
    overtime_hours = hours_worked - 40 #calculate overtime hours 
    overtime_pay = overtime_hours * (pay_rate * 1.5) # overtime pay uses 1.5x rate
    gross_pay = regular_pay + overtime_pay # Total gross pay
    print("You worked more than 40 hours. Overtime pay applies")
elif hours_worked == 40:
    gross_pay = hours_worked * pay_rate 
    print("You worked exactly 40 hours. No overtime.")
else: 
    gross_pay = hours_worked * pay_rate #If hours are 40 or less, no overtime
    print("Your worked less than 40 hours. No overtime.")
 

print(f"Gross pay is ${format(gross_pay, '.2f')}")
