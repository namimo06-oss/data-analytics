#LAB 1 -- Converting from Fahrenheit to Celsius 

fahrenheit = float(input("Enter temperature in Farenheit: ")) #input a temp in F
celsius = (fahrenheit - 32) * 5/9 #formula to convert F to C
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C") #print result within 2 decimal places
      
