# LAB 1 
#CONVERT DEPARTMENT CODE INTO A DEPARMENT NAME 
# Departments: marketing, human resources, accounting, legal, IT and customer relations

# ask for department code
dept_code = int(input("Enter department code: "))

# check department code

if dept_code == 8:
    print("Marketing")
elif dept_code == 12:
    print("Human Resources")
elif dept_code == 14:
    print("Accounting ")
elif dept_code == 16:
    print("Legal")
elif dept_code == 18:
    print("IT")
elif dept_code == 20:
    print("Customer Relations")

else:
    print("Invalid department code.")    #Runs if code does not match any options 

