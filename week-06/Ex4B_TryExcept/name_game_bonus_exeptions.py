# NAME GAME WITH EXCEPTIONS

# Ask the user for a name
name = input("Enter a name: ")
# Try block tests for possible errors
try:
    # Check if user entered nothing
    if name == "":
        raise ValueError("You cannot leave the name blank")
    # Check if input contains only letters and spaces
    if not name.replace(" ", "").isalpha():
        raise TypeError("Name must contain only letters")
    # Function to shorten the name
    def trunc_name(name):
        # Convert to lowercase
        name = name.lower()
        # Split name into words
        parts = name.split()
        # First word only
        first = parts[0]
        # If first letter is vowel
        if first[0] in "aeiou":
            return first
        # If first two letters are consonants
        elif first[1] not in "aeiou":
            return first[2:]
        # Otherwise remove first consonant
        else:
            return first[1:]
    # Generator function
    def name_game(name):
        # Get shortened version
        short = trunc_name(name)
        # Yield each line of the song
        yield f"{name}, {name}, bo-b{short}"
        yield f"banana fana fo-f{short}"
        yield f"fee fi mo-m{short}"
        yield f"{name}!"
    # Print the song
    for line in name_game(name):
        print(line)
# Runs if ValueError happens
except ValueError as e:
    print(f"ValueError: {e}")
# Runs if TypeError happens
except TypeError as e:
    print(f"TypeError: {e}")
# Runs for any other unexpected error
except Exception as e:
    print(f"Unexpected error: {e}")
# Runs if no error occurs
else:
    print("The Name Game worked successfully!")
# Always runs
finally:
    print("Thanks for playing the Name Game!")
