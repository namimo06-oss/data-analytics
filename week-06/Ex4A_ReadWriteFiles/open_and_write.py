# Open file in append mode
# "a" means append (add new text to the end)

f = open("about_me.txt", "a")

# add new text to file
# \n creates a new line

f.write("\n")

f.write("Perfect night out: ")

f.write(
    "I would go to a rooftop restaurant with friends,"
    "eat good food, and then walk around the city at night.\n"
)

# Close the file
# Always close files when finished

f.close()