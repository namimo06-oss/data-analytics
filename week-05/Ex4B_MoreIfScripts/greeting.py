#LAB 2

# ask for current hour
current_hour = int(input("Enter current hour (0-23):"))

# Check time conditions 

# Special late-night condition
if current_hour >= 23 or current_hour < 4:
    print("What are you doing up so late??")

elif current_hour < 10: #morning
    print("Good morning!")

elif current_hour < 17: #daytime
    print("Good day!")

else: #evening
    print("Good evening!")
