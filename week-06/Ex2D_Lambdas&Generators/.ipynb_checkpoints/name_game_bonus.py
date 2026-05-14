# Ask user for a name
name = input("Enter a name: ")

# Function to truncate name
def trunc_name(name):
    # Convert to lowercase
    name = name.lower()
    # List of vowels
    vowels = "aeiou"
    # If first letter is vowel
    if name[0] in vowels:
        return name
    # If first 2 letters are consonants
    elif name[0] not in vowels and name[1] not in vowels:
        return name[2:]
    # Otherwise remove first consonant
    else:
        return name[1:]

# Generator function
def name_game(name):
    # Get truncated name
    short = trunc_name(name)
    # Convert original name to title case
    proper_name = name.title()
    # Yield song lines
    yield f"{proper_name}, {proper_name}, bo-b{short}"
    yield f"Banana-fana fo-f{short}"
    yield f"Fee-fi-mo-m{short}"
    yield f"{proper_name}!"


# Print song
for line in name_game(name):
    print(line)
