# class notes 05/08/26

#greeting script 

greeting = input ("Enter hi")

print(f'You entered {greeting}')

print(f'The first two letters are {greeting[:2]}')

if greeting[:2].lower() == 'hi': # added index range and .lower method so that HI or Hi!!!!! also works
    print("Hello there!")
else:
    print("Rude.")


#ANOTHER EXAMPLE
greeting = input("Hi! (Enter greeting:)")

alt_greetings= ["hi","hello","hey","sup","yo","hiii","howdy"] #we going to chnage [] for {} so it can be unordered 

print(f'You entered {greeting}')

greeting = greeting.replace("!","").replace(",","").replace(".","").lower()

if greeting in alt_greetings:
    greet, *_ = alt_greetings #unpacking collection
    print(greet) #no slicing allow because it is unordered  
else:
    print("Rude.")

#use if /elif/else to assign letter grades 
score = int(input("What is the raw score? (Enter a number)"))
grade = none
#print(type(score))
if score == 100:
    grade = 'A+' 
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60: 
    grade = 'D'
else:
    print("Retake required.")

print(f'Grade is {grade}')


