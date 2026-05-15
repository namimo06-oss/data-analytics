# VALUE ERROR EXAMPLE
try:
    # Trying to convert letters into an integer
    num = int("hello")
except ValueError:
    # Runs if ValueError happens
    print("ValueError: Cannot convert text into a number")
else:
    # Runs if no error occurs
    print(num)
finally:
    # Always runs
    print("Let's try another one...\n")

# ANOTHER VALUE ERROR EXAMPLE
try:
    # Asking user for a number
    age = int("twenty")
except ValueError:
    print("ValueError: You must enter a valid number")
else:
    print(age)
finally:
    print("Let's try another one...\n")


# NAME ERROR EXAMPLE
try:
    # Variable does not exist
    print(banana)
except NameError:
    print("NameError: Variable is not defined")
else:
    print("No error")
finally:
    print("Let's try another one...\n")

# ANOTHER NAME ERROR EXAMPLE
try:
    # Trying to use undefined variable
    total = apples + oranges
except NameError:
    print("NameError: One or more variables do not exist")
else:
    print(total)
finally:
    print("Let's try another one...\n")


# TYPE ERROR EXAMPLE
try:
    # Cannot add string and integer together
    result = "5" + 5
except TypeError:
    print("TypeError: Cannot combine string and integer")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# ANOTHER TYPE ERROR EXAMPLE
try:
    # Cannot divide text
    answer = "hello" / 2
except TypeError:
    print("TypeError: Unsupported operation for strings")
else:
    print(answer)
finally:
    print("Let's try another one...\n")


# SYNTAX ERROR EXAMPLE
try:
    # eval() runs the code as Python code
    eval("if 5 > 2 print('hello')")
except SyntaxError:
    print("SyntaxError: Invalid Python syntax")
else:
    print("Code worked")
finally:
    print("Let's try another one...\n")

# ANOTHER SYNTAX ERROR EXAMPLE
try:
    # Missing closing parenthesis
    eval("print('hello'")
except SyntaxError:
    print("SyntaxError: Missing symbol or incorrect syntax")
else:
    print("Code worked")
finally:
    print("Let's try another one...\n")
