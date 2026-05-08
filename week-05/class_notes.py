#notes 05/07/2026
#TUPLES--fixed collection of valuess defined within parenthesis, unchangeable

#compare list to tuple
groceries = ["milk", "eggs", "almond yogurt", "bread"]
groceries.insert(1,"brownies")
print(groceries)


#Creating a tuple
print()
print('Here is our tuple set of steps:')
groc_tup = ("milk","eggs","almond yogurt", "bread")
groc_tup = list(groc_tup) #reassign ????
print(groc_tup)
groc_tup.append("brownies")
groc_tup = tuple(groc_tup)

print(groc_tup[-1])
print(groc_tup)
            
#list has build options so you can change it but tuples are mean to not be change
#it helps stopping mishaps with functions that interact with the tuple as well

#example of unpacking 

print()
print("Working with unpacking")

print(groc_tup)

m,b,e,ay,br = groc_tup  #assing a _ to the things you dont care about ex:m, b, _, _,_= groceries
#variable name can be whatever you want 
print(m)
print(b)


x,y, *z= groc_tup
print(f'the value of x is {x}')
print(f'the value of y is {y}')
print(f'the remaining values are {z}')

a,b,c= (1,2,3)

print(f'{c},{b},{a}')


#tuple concatenation
print()
print("starting tuple", groc_tup)

mike_groc = ("peanut butter", "caramel", "chocolate chip cookie")

groc_tup += mike_groc

print("Now with Mike's grocery request", groc_tup)

kevin_groc = ("salad",) #need comma to make a tuple of 1 item

groc_tup += kevin_groc

print("Plus Kevin's salad", groc_tup)

#working with sets
print()
print("Creating a seating arrangment:")

attendees={"Natalia", "Stefanie","Brandon", "Dahlia"}

seat1,seat2,seat3,seat4 = attendees

print (f'Table 1 seats: {seat1}, {seat2}, {seat3}, {seat4}')

rsvp = ["Brandon", "Dahlia", "Destiney", "Edmund"]

attendees.update(rsvp)

print(f"Updated for RSVPs: {attendees}")

attendees.add("Hritik") #to add to the set 

print(f'One more for the guest list:{attendees}')

#list: ordered, mutable, allows duplicates-- enclosed in []
#tuple:ordered, immutable, allows duplicares -- enclosed in ()
#set: unordered, semi-immutable, does not allow duplicates-- enclosed in {}
    
#working with dictionaries pg 62 work book 
    #use {}
    #store values in pairs 
    #ordered, changeable and no duplicates allow 

print()
print("Dahlia's car")

dahlia_car= {
    "make":"Nissan",
    "model": "Rogue",
    "year" : 2022,
    "color": "gray"
}

print(dahlia_car)
print(f'Dahlia owns a {dahlia_car['year']}{dahlia_car['make']}{dahlia_car['model']}')

parking_spaces = {1: 'Greg', 2:'Sal', 3: 'Casey'}

print(f'Parking space 1 is assigned to {parking_spaces[1]}')

print(parking_spaces.items())
print(parking_spaces.keys())
print(parking_spaces.values())

print(f'Parking space 4 is assigned to {parking_spaces.get(4,'[no space available]')}')

#add new item or space in this case 

parking_spaces[4]='Herman'
print(f'Parking space 4 is assigned to {parking_spaces.get(4,'[no space available]')}')

print(4 in parking_spaces)
print("Herman" in parking_spaces)
print(parking_spaces)

#nested collections 
print()

print("working with nested collections")

#when might this be useful?
#biology: body>organ>cell
#geography: state>county>city>municipal district > neighborhoog 
#taxonomy:kingdom>phylum>class>order>family>genus>species 
#spreadsheets: a documeny with multiple rows (or columns)
# entity relationship diagram

employee= (
    ("emp_id","name","hire date", "salary"),
    ('007', "James Bond", "Nov 30, 2005", 128000),
    ('008', "Miss Moneypenny", "Apr 4, 2008", 148000),
    ('100',"Quigley Henry", "May 5,2015", 178000)
)

print(f'This year the employee picnic is being run by {employee[1][1][0:5]}')


#MODULE 4 if,elif,else

#using if/else

groceries = ["milk", "eggs", "almond yogurt", "bread"]

groc_check = input("Check for item on grocery list:")

if "eggs" in groceries:
    print("Grocery list contains eggs")
else:
    print("Not on grocery list")

if groc_check in groceries:
    print(f"Groceries list contains {groc_check}")
else:
    print("Not on grocery list")
    groceries.append(groc_check) # append is to add to an existing list
    print(f'{groc_check} has been added to list')

print(f"Grocery list:{groceries}")

#conditions are read top-down -- as soon as a condition returns true, if/else block is done

print()
print("Grocery basket cost")

grocery_budget = 100

basket=[10, 15, 10, 15, 20, 25]

if sum(basket) < grocery_budget:
    print(f"Keep shopping - #{grocery_budget - sum(basket)}left")
elif (grocery_budget - sum(basket)) < 10:
    print("Caution: you have less than $10")







