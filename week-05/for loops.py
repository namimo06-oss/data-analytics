#working with for loops

for i in 'banana':
    print (i)

for i in ['banana', 'apple', 'pear']:
    print(i)

for i in ['banana', 'apple', 'pear']:
    for x in i:
        print(x) #spell letter by letter of each fruit 

for i in range(5,10):
    print(i)  #starting on 5 and up to but not including 10

#back to groceries
grocery_list = ["peach","apple","chocolate chip cookies","rotisserie chicken", "pita"]

in_stock = ("pita", "cake", "bread", "peach", "apple", "ground beef", "chocolate chip cookies") 
basket = []

for current_item_in_list in grocery_list: # needs to end with :
   if current_item_in_list in in_stock:
      basket.append(current_item_in_list)
    else:
       print(f'Not found:{current_item_in_list}')
       print("Go back and check your list again")
       break
   

print(basket)
