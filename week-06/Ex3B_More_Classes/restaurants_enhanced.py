
# Restaurant class

class Restaurant:
    '''
    This class stores restaurant information,
    tracks customers served,
    and stores customer ratings.
    '''
    # Constructor method
    def __init__(self, rest_name, food_type):
        # Restaurant information
        self.rest_name = rest_name
        self.food_type = food_type

        # Default attributes
        self.number_served = 0
        self.customer_ratings = []

    # Describe restaurant
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    # Restaurant open message
    def rest_open(self):
        print(f"{self.rest_name} is open.")

    # Add customers served
    def add_num_served(self):
        # Ask user for customer amount
        customers = int(input("How many customers served today? "))
        # Add to total
        self.number_served += customers

    # Print total customers served
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    # Add customer ratings
    def customer_rating(self):
        # Infinite loop until valid input
        while True:
            # Ask user for rating
            rating = input(
                "How would you rate your experience today on a scale of 1-5? "
            )
            # Check if input is numeric
            if rating.isdigit():
                # Convert to integer
                rating = int(rating)
                # Check valid range
                if rating >= 1 and rating <= 5:
                    # Add rating to list
                    self.customer_ratings.append(rating)
                    # Calculate average
                    average = (
                        sum(self.customer_ratings)
                        / len(self.customer_ratings)
                    )
                    # Print result
                    print(
                        f"Your rating was {rating}. "
                        f"The average rating for this restaurant is "
                        f"{format(average, '.2f')}"
                    )
                    # Exit loop
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            else:
                print("Invalid input. Please enter a whole number 1-5.")

# Create restaurant objects
rest1 = Restaurant("Inoot-Ut Brubge", "burgers")
rest2 = Restaurant("Weedy's", "fast food")
rest3 = Restaurant("Applebapple's", "breakfast food")

# Test restaurant 1
rest1.print_num_served()
rest1.add_num_served()
rest1.add_num_served()
rest1.print_num_served()
print()
rest1.customer_rating()
rest1.customer_rating()
print()


# Test restaurant 2
rest2.print_num_served()
rest2.add_num_served()
rest2.print_num_served()
print()
rest2.customer_rating()
print()


# Test restaurant 3
rest3.print_num_served()
rest3.add_num_served()
rest3.print_num_served()
print()
rest3.customer_rating()
