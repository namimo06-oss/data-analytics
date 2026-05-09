# BONUS LAB
# Gregorian Calendar -- how to determine a leap year

year = int(input("Enter a year:"))

# Leap year rules:
# divisible by 4 
# BUT years divisible by 100 are NOT leap years
# UNLESS divisible by 400
if year % 400 == 0:  #we must check 400 first 
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is NOT a leap year")
elif year % 4 == 0: # this condition must be the last one so it can check the other ones first, if we put this one first then pyhton won't check for the other conditions 
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")
