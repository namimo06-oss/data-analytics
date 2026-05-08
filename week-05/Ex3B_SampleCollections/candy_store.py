#LAB 2
# Creating tuples 
# Tuples use parenthesis ()
candies = ("Gummy Bears", "Lollipops", "Jelly Beans")
flavors = ("Lychewatermelon", "mangococo", "matcha") #tuple of flavors

# Create a set to store combinations
candy_combinations = set() 

# Add combinations using tuple indexing
candy_combinations.add((candies[0], flavors[0]))  # gummy bears + lychewatermelon
candy_combinations.add((candies[1], flavors[1]))  # jelly beans + mangococo
candy_combinations.add((candies[2], flavors[2]))  # hard candy + matcha

# Output message
print("Today's candy options include:")
print(candy_combinations)

# Print multiple times to observe order
print("\nPrinting again:")
print(candy_combinations)
print("\nPrinting again:")
print(candy_combinations)

# Note:
# Sets do NOT keep order, so output may change each time conceptually
