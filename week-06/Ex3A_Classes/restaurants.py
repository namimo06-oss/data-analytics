# Restaurant class
class Restaurant:
    '''
    This class stores restaurant information
    and displays restaurant messages.
    '''

    # Constructor method
    # Runs automatically when object is created
    def __init__(self, rest_name, food_type):
        # Instance variables
        # Stored separately for each object
        self.rest_name = rest_name
        self.food_type = food_type
    
    # Method to describe restaurant
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    
    # Method to show restaurant is open 
    def rest_open(self):
        print(f"{self.rest_name} is open.")
    
# Create restaurant objects 
rest1 = Restaurant("Inoot-Ut Brubge", "burgers")
rest2 = Restaurant("Weedy's", "fast food")
rest3 = Restaurant("Applebapple's", "breakfast food")

# Call methods for restaurant 1
rest1.describe_rest()
rest1.rest_open()
print()

# Call methods for restaurant 2
rest2.describe_rest()
rest2.rest_open()
print()

# Call methods for restaurant 3
rest3.describe_rest()
rest3.rest_open()
