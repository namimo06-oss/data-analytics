#LAB 1 -- Calculate distance btw coordinates 
#This program calculates distance between two points (x1,y1) and (x2, y2)

import math  #Import math module to use square root function

#Get first point coordinates from user 
x1= float(input("Enter x1: "))
y1= float(input("Enter y1:"))

#Get second point coordinates from user 
x2= float(input("Enter x2: "))
y2= float(input("Enter y2:"))

#Apply distance formula:
# sqrt((x2-x1)^2 + (y2-y1)^2)
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2) # use ** for exponent(power)

print(f"The distance between the point is {format(distance, '.2f')}") # to print final result