#LAB 1 
import math  # for rounding up

people = int(input("How many people are going on the tour? "))# Ask how many people are going

capacity_per_van = 15 # Each van holds 15 people

vans_needed = people / capacity_per_van# Calculate how many vans are needed

vans_needed = math.ceil(vans_needed) # Round up because you can't rent partial vans

cost_per_van = 250 # Cost per van per day

total_cost = vans_needed * cost_per_van # Total cost of all vans

cost_per_person = total_cost / people # Cost per person

# Print results
print(f"Number of vans needed: {vans_needed}")
print(f"Total cost of vans: ${format(total_cost, '.2f')}")
print(f"Cost per person: ${format(cost_per_person, '.2f')}")

# For 38 people the cost was $19.74, and $750 were collected. The vans were $750
# You have money left because 3 vans= 45 seats, so 7 seats empty. You ran up vans, so you will have empty seats. 