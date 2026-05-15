# Open file in read mode
# "r" means read

f = open("about_me.txt", "r")

# Read FULL file 
print(f.read())

# close file
f.close()


#  USING .read(50)
f = open("about_me.txt", "r")
# Read first 50 characters
print(f.read(50))
# Read NEXT 50 characters
print(f.read(50))
# close file
f.close()


# USING .readline()
# Open file 
f = open("about_me.txt", "r")
# Read first 10 characters of first line
print(f.readline(10))
# Read rest of the first line
print(f.readline())
#Loop through next 4 lines
for i in range(1,5):
    print(f.readline())
# close file
f.close()


# USING .readlines()
# Open file
f = open("about_me.txt", "r")
# Read lines into list
print(f.readlines(1))
print(f.readlines(1))
print(f.readlines(10))
#close file
f.close()


# COMBINING DIFFERENT TYPES OF READING 
#Open file
f = open("about_me.txt", "r")

# First 50 characters
first_50 = f.read(50)

# Store next 4 lines in a list
next_lines = []
for i in range(4):
    next_lines.append(f.readline())

# Read next 100 characters as list by line
next_100 = f.readlines(100)

# Print results
print(f"First 50 characters: {first_50}")
print()
print(f"Next four lines, as list by line: {next_lines}")
print()
print(
    f"Next 100 characters, as list by line, "
    f"rounded up to complete lines: {next_100}"
)

# Close file
f.close()
