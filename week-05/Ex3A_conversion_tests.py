# Description: This script tests various numeric
#             convertion techniques
# Author: Sam Q. Newprogrammer 

a = " 101.1 " # with spaces before and after    
b = '55' #clean numeric string
c = "402 Stevens" # string with number and text
d = 'Number 5  ' #with spaces after 5 

#USING .strip()
#removes spaces from the beginning and end of a string 

#strip spaces where needed
a_stripped = a.strip() #becomes "101.1"
b_stripped = b.strip() 
c_stripped = c.strip()
d_stripped = d.strip() #becomes 'Number 5'

print("Original values and types:")
print(a, type(a))
print(b, type(b))
print(c, type (c))
print(d, type(d))


# CONVERSIONS

# Variable a 
# Cannot convert directly to int because it has a decimal int(a_clean) #valueerror
a_float = float(a_stripped)  #converts string to float 
a_int_from_float = int(float(a_stripped)) #converts float to integer


# Variable b
# This string contains only numbers, so both work 
b_int = int(b_stripped)
b_float = float(b_stripped)


# Variable c
# These conversions fail because the string contains letters 
# c_int = int(c_stripped)  # ValueError: invalid literal for int()
# c_float = float(c_stripped)  # ValueError: could not convert string to float


# Variable d
# These convertions also fail because the string contains text 
# d_int = int(d_stripped)  # ValueError: invalid literal for int()
# d_float = float(d_stripped)  # ValueError: could not convert string to float

 
# PRINT RESULTS

print("\nConversions results:")

print("a float:", a_float, type(a_float))
print("a int from float:", a_int_from_float, type(a_int_from_float))

print("b int:", b_int, type(b_int))
print("b float:", b_float, type(b_float))

print("c original:", c, type(c))

print("d original:", d, type(d))

# NOTES (as required by lab)
# a)
# int(a_stripped) -> ERROR: ValueError (cannot directly convert string with decimal)
# float(a_stripped) -> works
# int(float(a_stripped)) -> works

# b)
# int(b_stripped) -> works
# float(b_stripped) -> works

# c)
# Both int() and float() fail because of text ("Stevens")

# d)
# Both int() and float() fail because of text ("Number")

# PART d - USING SLICING

# Variable c = "402 Stevens"
# Take only the numeric portion "402"
c_number = c[0:3]     # characters from index 0 up to 3
c_int = int(c_number) # convert string to integer

# Variable d = "Number 5 "
# Take only the number "5"
d_number = d[7]       # character at index 7
d_int = int(d_number) # convert string to integer

print("\nSlicing results:")
print(c_number, type(c_number))
print(c_int, type(c_int))

print(d_number, type(d_number))
print(d_int, type(d_int))


# PART e - USING .strip()
# .strip() removes spaces from the beginning
# and end of a string
print("\nUsing strip():")
print(a.strip())
print(d.strip())
