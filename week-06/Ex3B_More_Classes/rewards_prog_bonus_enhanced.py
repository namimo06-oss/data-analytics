# LAB 2 OPTIONAL 
# Global customer list
cust_list = []

# Rewards Program Class
class RewardsProgram:
    '''
    This class stores customer rewards information
    and tracks restaurant visits and rewards points.
    '''
    # Constructor
    def __init__(self, cust_name, phone, email):

        # Customer information
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

        # Default attributes
        self.restaurants_visited = []
        self.rewards_points = 0

    # Print customer profile
    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    # Thank you message
    def thank_you(self):
        print(
            f"Thank you, {self.cust_name}, for visiting our restaurant!"
        )

    # Add customer to global list
    def add_to_cust_list(self):
        cust_list.append(
            (self.cust_name, self.phone, self.email)
        )

    # Visit restaurant method
    def visit_rest(self):
        # Ask restaurant name
        restaurant = input("Name of restaurant: ")
        # Check if restaurant already exists
        if restaurant not in self.restaurants_visited:
            # Add restaurant to list
            self.restaurants_visited.append(restaurant)
        # Ask food bill amount
        bill = float(
            input("What was the total food bill for this visit? ")
        )
        # Calculate rewards points
        points = int(bill)
        # Add points to total balance
        self.rewards_points += points
        # Print results
        print(f"Points for this visit: {points}")
        print(
            f"Total rewards points earned: "
            f"{self.rewards_points}"
        )
        print(
            f"Thank you for visiting {restaurant}!"
        )


# Create customer objects
cust1 = RewardsProgram(
    "Natalia Miranda",
    "555-1234",
    "natalia@email.com"
)
cust2 = RewardsProgram(
    "Sophia Lee",
    "555-7777",
    "sophia@email.com"
)
cust3 = RewardsProgram(
    "Daniel Kim",
    "555-8888",
    "daniel@email.com"
)


# Test customer 1
cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()
cust1.visit_rest()
print()

# Test customer 2
cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()
cust2.visit_rest()
print()

# Test customer 3
cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()
cust3.visit_rest()
print()

# Print customer list
print("Customer List:")
print(cust_list)
