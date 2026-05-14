# Lambda functions

# Create lambda function
# n = parameter
# n * 2 = return value
doubler = lambda n: n * 2

# Test doubler
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Tripler lambda
tripler = lambda n: n * 3

# Test tripler
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# Function that creates multiplier lambdas

def multiplier(x):
    # Return lambda function
    return lambda n: n * x

# Create multipliers

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


# Test new multiplier variables

print(quadrupler(2))
print(quintupler(3))
print(sextupler(4))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))
