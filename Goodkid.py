"""
Author: Darian Porch
File: Goodkid.py
Description: 
This app accepts students names and GPAs and determines if the student
for the Dean's List of the Honor Roll. It continues to accept student
until the last name 'ZZZ' is entered.
"""


# Start an infinite loop to process student records
while True:
    # Ask for student's last name
    last_name = input("Enter student's last name (or 'ZZZ' to quit):") 

    # Quit if last name is 'ZZZ'
    if last_name.upper() == "ZZZ":
        print("Exiting program.")
        break

    # Ask for student's first name
    first_name = input("Enter student's first name")

    # Ask for GPA and convert to float
    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a number.")
        continue

    # Check Dean's List eligibility 
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")

    # Check Honor Roll eligibility
    if gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll!")

    print("-" * 40)  #Separator for readability