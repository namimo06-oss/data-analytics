#LAB 2

# Messy contact records
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# Converting all 3 names to lowercase using .lower()
print(name_1.lower())
print(name_2.lower()) # converts all letters to lower case
print(name_3.lower())

#Converting all 3 names to title case .title()
print(name_1.title())
print(name_2.title()) # capitalizes first letter of each word
print(name_3.title())

# Using .replace () to remove $
clean_salary_1 = salary_1.replace("$","")
clean_salary_2= salary_2.replace("$","")

print(clean_salary_1)
print(clean_salary_2)

# check the data tyoe after removing $
# they are still strings because they contain text characters 
print(type(clean_salary_1))
print(type(clean_salary_2))
# To perferom math, we would need to convert them to numbers 
# The commas must also be removed before using int()


# Chain .replace() and int() together
salary_number1 = int(salary_1.replace("$","").replace(",",""))

# print cleaned integer value
print(salary_number1)

#confirm the new data type
print(type(salary_number1))
