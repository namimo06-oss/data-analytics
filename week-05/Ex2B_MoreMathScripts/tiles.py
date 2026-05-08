#LAB 1 -- calculating how many boxes of tiles are needed for a room
import math #we use this for rounding up (ceil)

#asking to input dimensions
length = float(input("Enter room length in feet:"))
width = float(input("Enter room width in feet:"))

area = length * width #calculate total area (this equals number of tiles needed) find area

tiles_needed = area * 1.10 # Add 10% extra tiles -- 100 = 1.00 --10%=0.10 -- 1.00+0.10 =1.10

boxes_needed = math.ceil(tiles_needed/12) #convert tiles to boxes (12 per box)

#print results
print("Tiles needed (with 10% extra):", tiles_needed)
print("Total boxes required:", boxes_needed)

