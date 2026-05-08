#LAB 1

salary = float(input("Enter your montly salary:")) #ask user for their salary 
taxes = salary * 0.23 #calculate 23% taxes
net_income = salary - taxes #money left after taxes 

print (f"Your salary is {format(salary, '.2f')}")
print (f"Taxes withheld are {format(taxes, '.2f')}")
print (f"Your net income is {format(net_income, '.2f')}")