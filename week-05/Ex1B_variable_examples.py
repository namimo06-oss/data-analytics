# LAB 1
# Customer information variables 
customer_id = "7700" # I assumed to be a string because it's and identifier, not used for calculations
customers_name = "John White" # I assumed full name in one variable, but could be split into first and last name
customer_gender = "male" # I assumed a single value, but in real systems could use codes (F/M/O or dropdown options)
customer_date_of_birth = "1995-06-15" # Stored as string; could also be stored as a date type for calculations (age)
drivers_license_number = "D0273728" #Assumed alphanumeric identifier, not meant for math operations.
auto_policy_number = "POL9384777" # Assumed string ID; format may vary depending on insurance company.

# Variables for my own
my_first_name = "Natalia" 
my_last_name = "Miranda" 
birth_city = "Bogota"
birth_country = "Colombia" 

# LAB 2
# Full list of reserved words that can't be used for variables names.
#1. False, de, if, ^raise^, none, del, import , return, true, elif, in, try, and, else, is, ^while^, as, ^except, lambda^,
# with, ^assert, finally, nonlocal, yield, break, for, not, class, form, or, continue, global, pass.^
import keyword
print (keyword.kwlist)
#2. DEFINITIONS
# raise: is used to raise an error. These errors are visible in the traceback and they cancel the execution of the program if not handled properly.
# while: this statement is used to start a while loop. It continues iteration until a condition is no longer True.
# except: part of the type... except errorhandling structure in Python. Tells what to do when an exception occurs.
# lambda: is an anonymous function. It can take any number of arguments but only have a single expression. 
# nonlocal: is used in functions inside functions to create anonymous functions.




