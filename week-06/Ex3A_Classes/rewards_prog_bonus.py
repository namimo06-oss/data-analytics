# LAB 2
# Global customer list

# Created ONCE outside the class
# so data is not overwritten
cust_list = []

# Rewards Program class
class RewardsProgram:
    '''
    This class stores customer information
    for a restaurant rewards program.
    '''
    # Constructor
    def __init__(self, cust_name, phone, email):
        # store customer data
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
    
    # Display customer profile
    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
    
    # Thank customer
    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")
    
    # Add customer to list
    def add_to_cust_list(self):
        # create tuple
        customer_data = (
            self.cust_name,
            self.phone,
            self.email
        )

        # Append tuple to global list
        cust_list.append(customer_data)

# Create customer objects
cust1 = RewardsProgram(
    "Natalia Miranda",
    "555-1234",
    "natalia@email.com"
)

cust2 = RewardsProgram(
    "Sophia Lee",
    "555-5678",
    "sophia@email.com"
)

cust3 = RewardsProgram(
    "Daniel Kim",
    "555-9999",
    "daniel@email.com"
)

# Run methods for customer 1
cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()
print()

# Run methods for customer 2
cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()
print()

# Run methods for customer 3
cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()
print()


# Print customer list
print(cust_list)
