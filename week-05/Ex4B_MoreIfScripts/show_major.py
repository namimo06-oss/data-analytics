# LAB 5
# SHOW MAJOR LOOKUP SCRIPT

# student information
student_name = "Natalia Miranda"
student_major = "BIOL"

# test 1
student_name = "Jose Balvin"
student_major = "ENG"

# test 2
student_name = "Vanessa White"
student_major = "BUSS"

#Test 3
student_name = "Luis Navarro"
student_major = "HIST"


#LOOKUP LOGIC 
if student_major == "BIOL":
    major_name = "Biology"
    department_office = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    department_office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    department_office = "Kerr Hall, Room 201 "
elif student_major == "HIST":
    major_name = "History"
    department_office = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    department_office = "Westly HalL, Room 310"
else:
    major_name = "Unknown Major" #if major not include in the table 
    department_office = "N/A"

#OUTPUT
print("Student Name:", student_name)
print("Major Code:", student_major)
print("Major Name:", major_name)
print("Office Location:", department_office)
