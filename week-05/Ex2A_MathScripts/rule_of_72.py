#LAB 2
#Rule of 72 calculation
# It estimates how many years it takes for money to double based on an annual interest rate. 

current_savings= 5000
interest_rate = 6#this variable stores the interest rate as a decimal -- 6% in python is equal to .06 because 6/100=0.06

years= 72/interest_rate #rule of 72 formula-- result was 12 which means money takes 12 years to duplicate 
doubled_balance = current_savings * 2 #this calculates the double amount of money

print ("Your current saving is " + format(current_savings, ".2f")) #displays the current savings with 2 decimal places 

print(
    f"At a {interest_rate}% interest rate, "
    f"your savings account will be worth "
    f"{format(doubled_balance, '.2f')} "
    f"in {format(years, '.1f')} years"
)

#LAB 3 

#Ask the current user for their current saving amount
#input() lets the user type a value in the terminal
current_savings= float(input("What is your current savings amount? ")) #float() converts the text into a number with decimals


#Ask the user for the interest rate 
#The user should enter a whole number like 6 for 6%
interest_rate = float(input("What is the interest rate?"))

#rule of 72 formula
years= 72 /interest_rate #divide 72 by the interest rate to estimate the years needed to double savings

doubled_balance = current_savings * 2 #multiply saving by 2 to find the doubled balance 


print(f"Your current savings is {format(current_savings, '.2f')}") #display current savings amount


print(
    f"At a {interest_rate}% interest rate,"
    f"your saving account will be worth"
   f" {format (doubled_balance, '.2f')}"
   f"in {format(years, '.1f')} years"
) 

#Possible pitfall:
# input() always returns text, so float () is needed for calculations
# the program may crash if the user enters letters instead of numbers 