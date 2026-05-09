# LAB 4
# MIN AND MAX OF THREE NUMBERS 

# Test values 
a = 17
b = 22
c = 77

# Finding smallest number
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Smallest number is:", smallest)

# Finding largest number 
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Large number is:", largest)