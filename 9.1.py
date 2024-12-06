"""
script: Grade average and txt writer
action: This script will allow the user to input different grades for students and will put them on a txt file as well
as calculate the average while also allowing the user to quit out.
author: Cesar Ulises Valenzuela
Date: 12/5/2024
"""
from pathlib import Path


def find_mean(lst):
    """
    action: this function is the calculation for the mean of the students grades

    input: lst
    output: no printing
    return: the mean of the students grades
    """
    return sum(lst) / len(lst) if lst else 0


path = Path("grades.txt") # sets path

list_of_grades = [] # list where grades will be stored

prompt = "Please enter a student's grade" # prompt for input
prompt += '\nEnter "quit" to quit'

while True:
    grades = input(f"{prompt}: ")
    if grades.lower().strip() == "quit":  # sentinel Value
        print(f"The mean grade is: {find_mean(list_of_grades)}") # calls find_mean()
        break
    else:
        try:
            # Converts the input to an integer and append it to the list
            grade = int(grades)
            print(f"{grade} has been added")
            list_of_grades.append(grade)
        except ValueError:
            # if user input is not a number
            print("Please enter a valid number for the grade.")

# Prepare the grades for writing to the file
newline = ""
for grade in list_of_grades:
    newline += f"{grade}\n"

# Write to the file
path.write_text(newline)