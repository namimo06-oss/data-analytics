# LAB 2 
x = 100
y = 20

# PART A
# check if x divided by y equals 5
if x / y == 5:
    print("x divided by y is 5")
    # Change x to 1 if condition is true
    x = 1

else:
    print("are the variables set up correctly?")

# PART B 
# check if x times y equals y 
if x * y == y:
    print("now x times y is y")

    # Change x to 10
    x = 10
else:
    print(f"Whoops, x equals {x}")

# PART C
# check if x is less than y
if x < y:
    print("x is less than y")

    # Double the value of x
    x = x * 2
else:
    print("uh oh, x is not less than y")

# PART D
# Check is x is greater than y 
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

#PART E

# PRINT FINAL VALUES 
print(f"The final value of x is {x} and the final value of y is {y}")
