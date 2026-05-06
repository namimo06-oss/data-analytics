print('Hello World')

message= 'Hello world!'
print(message)

#"Hello world" prints twice because it runs the first print and then the second variable I did as well.
# two separate print statements = two outputs


# Displaying dollars and cents 
dollar = 3
cents = .50
print(dollar + cents)
# It added both values = 3.5. Python treats 3 as an integer and .50 as a float.
#Python prints 3.5, not 3.50, because:
#Trailing zeros in floats are not shown by default.
# 3.5 and 3.50 are mathematically the same value.
cents = cents + .25
print (dollar + cents)

d_str = '3 dollars'
c_str = '50 cents'
print (d_str + " " + c_str) #there most be an space within the quotes
