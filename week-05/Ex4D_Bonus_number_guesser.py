# BONUS PROJECT: NUMBER GUESSER
# GAME TIME!!!

import random # import random so we can shuffle a list 

number_pool = list(range(1,21)) #create a list of numbers from 1 to 20

random.shuffle(number_pool) # shuffle the list into random order

secret_number = number_pool[0] # pick the first number in the shuffle list

# Create a set to store guessed numbers
# Sets automatically avoid duplicates
guessed_numbers = set()

guess_count = 0 #keep track of number of guesses 

print("I am thinking of a number between 1 and 20.")

# START GAME LOOP
while True:
    player_input = input("Enter your guess:") #ask player for a guess

    if not player_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(player_input) #convert input into integer

    guessed_numbers.add(guess) #add guess to set 

    guess_count += 1 #increase guess counter

    #CHECK GUESS 
    if guess < secret_number:
        print("Higher")
    elif guess > secret_number:
        print("Lower")
    else:
        print("Correct! You guessed the number!") #correct guess

        print(f"It took you {guess_count} guesses.") #print total guesses 

        print(f"Your guesses were: {guessed_numbers}") #print all guessed numbers 

        if guess_count < 5:
            print("Awesome job!") #bonus message 

            break # end loop