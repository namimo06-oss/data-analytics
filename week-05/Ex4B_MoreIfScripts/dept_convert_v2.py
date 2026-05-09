# LAB 1 5 
# USING MATCH/CASE

dept_code = int(input("Enter department code: "))

# match department code
match dept_code:
    case 8:
        print("Marketing")
    case 12:
        print("Human Resources")
    case 14:
        print("Accounting")
    case 16:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    
    case _: # this is like else:
        #default case if nothing matches 
        print("Invalid department code")

# I compared with Destiney and we both did it the same way, pretty similiar just with different numbers.
# For me if/elif/else is easier for me , but I think match/case looks better and easiest to read and understand.
# no changes