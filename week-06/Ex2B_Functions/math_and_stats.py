# import modules
import random
import math
import statistics

# starting variables
vals_1_100 = range (1,100) # range from 1 to 99
vals_sample = random.sample(vals_1_100, 75) #random sample of 75 UNIQUE values
vals_choices = random.choices(vals_1_100, k = 200) # random selection of 200 values # choice() allows duplicates 
radius = random.randint(3,10) #random radius btw 3 and 10
pi = math.pi # store pi value

# Calculations for 75 sample values 

# Sum of values
sample_sum = sum(vals_sample)
# Average/ mean
sample_average = statistics.mean(vals_sample)
# Median
sample_median = statistics.median(vals_sample)

# Calculations for 200 values

# Mean
choices_average = statistics.mean(vals_choices)
# Median 
choices_median = statistics.median(vals_choices)
# Mode 
choices_mode = statistics.mode(vals_choices)
# Standard deviation
choices_stdev = statistics.stdev(vals_choices)
# Variance
choices_variance = statistics.variance(vals_choices)


# Circle calculations
# Formula:
# area = pi * radius squared
# radius squared = radius ** 2

circle_area = pi * (radius ** 2)

# Round UP
area_ceil = math.ceil(circle_area)

# Round DOWN
area_floor = math.floor(circle_area)

# Print output
print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_average}")
print(f"Median of 75 sample values: {sample_median}")

# Print blank line
print('\n')
print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {choices_average}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")

# Print blank line
print('\n')
print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_ceil} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_floor} (rounded down to the nearest integer)")

