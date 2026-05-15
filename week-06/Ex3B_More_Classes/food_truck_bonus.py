# LAB 3 OPTIONAL Parent class
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


class Restaurant:
    '''
    Parent restaurant class
    '''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

# Child class
class FoodTruck(Restaurant):
    '''
    Child class for food trucks
    '''
    def __init__(self, rest_name, food_type):
        # Call parent constructor
        super().__init__(rest_name, food_type)
        # Food truck attributes
        self.private_bookings = 'N'
        self.truck_location = ""
        # Store location history
        self.location_history = []
    # Private booking method
    def accepts_private_bookings(self):
        answer = input(
            "Does this food truck accept private bookings? Y/N "
        )
        self.private_bookings = answer.upper()
        if self.private_bookings == 'Y':
            print(
                "This food truck currently accepts private bookings."
            )
        else:
            print(
                "This food truck currently does not accept private bookings."
            )
    # Relocate truck
    def relocate_truck(self):
        location = input(
            "Enter current truck location: "
        )
        self.truck_location = location
        # Add location to history
        self.location_history.append(location)
        print(
            f"Truck is currently located at {self.truck_location}"
        )

# Create object
truck1 = FoodTruck("Taco Zoom", "Mexican food")

# Test methods
truck1.accepts_private_bookings()
print()
truck1.relocate_truck()
truck1.relocate_truck()
print()

# Print location history
print("Location History:")
print(truck1.location_history)
# I chose to include duplicate locations because food trucks may return to the
# same location multiple times during different events or business days.
