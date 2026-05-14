# Function 1: display_mailing_label()

# Create function with 5 parameters
def display_mailing_label(name, address, city, state, zip_code):
    #print formatted mailing label 
    print(name)
    print(address)
    print(f"{city}, {state}, {zip_code}")
    
    print()      #print blank line for spacing

# Function 2: add_numbers()

# *numbers means:
# accept ANY amount of arguments
def add_numbers(*numbers):
    total = sum(numbers) #add all numbers together

    # convert numbers into strings
    # so they can join together with +
    number_string = " + ".join(str(num) for num in numbers )

    # print formatted equation
    print(f"{number_string} = {total}")

# Function 3: display_receipt()
def display_receipt(total_due, amount_paid):
    #calculate difference 
    change_due = amount_paid - total_due

    # display totals formatted to 2 decimal places
    print(f"Total Due: ${format(total_due, '.2f')}")
    print(f"Amount Paid: ${format(amount_paid, '.2f')}")

    #if customer paid enough 
    if amount_paid >= total_due:
        print(f"Change Due: ${format(change_due, '.2f')}")

    #if customer still owes money
    else:
        # convert negative into positive 
        remaining_balance = total_due - amount_paid
        print(f"Remaining Balance: ${format(remaining_balance, '.2f')}")
    
    #blank line
    print()

# TESTING display_mailing_label()
display_mailing_label(
    "Natalia Miranda",
    "177 Main Street",
    "San Jose",
    "CA",
    "95132"
)

display_mailing_label(
    "Sophia Lee",
    "789 Will Rogers",
    "San Jose",
    "CA",
    "95117"
)

# TESTING add_numbers()

# one number 
add_numbers(5)
# Two numbers
add_numbers(5, 10)
# Multiple numbers
add_numbers(1, 2, 3, 4, 5)


# TESTING display_receipt()

# Overpay bill
display_receipt(25.50, 30.00)
# Exact payment
display_receipt(40.00, 40.00)
# Underpay bill
display_receipt(75.00, 50.00)



# BONUS mailing label function
# Allows optional second address line
def display_mailing_label2(
    name,
    address1,
    city,
    state,
    zip_code,
    address2=""
):
    print(name)
    print(address1)

    # Only print second address line if it exists
    if address2 != "":
        print(address2)
    print(f"{city}, {state} {zip_code}")

    print()


# Test bonus function
display_mailing_label2(
    "Natalia Miranda",
    "123 Main St",
    "Los Angeles",
    "CA",
    "90001",
    "Apartment 4B"
)
