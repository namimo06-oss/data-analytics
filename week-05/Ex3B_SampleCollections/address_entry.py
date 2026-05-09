#LAB 3
#create a dictionary 
# Dictionaries use curly brace{}

contact_info = {
    "name":"Natalia Monroy",
    "address": "792 Main Street",
    "city": "San Jose",
    "state": "CA",
    "zip": "95112"
}

# Print formatted mailing address

#Option 1 # triple quotes allow multi-line strings
#using f-string with newline characters 
print(f"""
Mailing Address:
{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]} """) #add a comma so the result can be San Jose, CA and spaces when need it 


# Option 2 alternative using \n = new line
print ("Mailing Address:\n"
    f"{contact_info["name"]}\n"
    f"{contact_info["address"]}\n"
    f"{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}")

#removing key:value pair for name 
del contact_info["name"]

# Adding new dictionary with new variable
full_name = {
    "first name" : "Natalia",
    "last name" : "Monroy"
}

#update full_name
#add a new key: value pair using .update()
full_name.update({
    "honorific" : "Ms."
})

# Add the full_name dictionary into contact_info
contact_info.update({
    "full_name": full_name
})

#PRINT UPDATED ADDRESS

print("Updated Address:")

print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}"""
)

