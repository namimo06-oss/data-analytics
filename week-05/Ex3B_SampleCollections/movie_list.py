# LAB 1
# Create a list of Favorites movies
# Lists use [] 
favorite_movies= [
    "The Fast and Furious:Tokyo Drift",  # don't forget the , if not it will take it as only one string 
    "The Notebook",
    "The Conjuring",
    "Taken",
    "Sinister"
]

# Using len() function to print descriptive statement 
print(f"The list favorite_movies includes my top {len(favorite_movies)} favorite movies")

# printing complete list
print(favorite_movies)

# using sorted()
print(sorted(favorite_movies))
print(favorite_movies)
# Observation: 
# sorted() creates a temporary sorted version
# It does NOT permantly change the original list

# Use .sort() to permanently sort the list 
favorite_movies.sort()

print(favorite_movies) # print list after sorting 

#Observation: .sort() permanently changes the original list while sorted() is temporary but doesn't changes the original list 

# Adding a new movie to the list using append()
favorite_movies.append("The Life List")

print(f"The list favorite_movies includes my top {len(favorite_movies)} favorite movies") #updated description 
print(favorite_movies) #updated list

#.append() adds a new item to the end of the list 
