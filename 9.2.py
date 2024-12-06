"""
script: average, count and sum, file reader
action: This script will read the previous file I made and return the total sum of the grades as well as return the
count of grades and the average from reading the file.
author: Cesar Ulises Valenzuela
Date: 12/5/2024
"""
from pathlib import Path

path = Path("grades.txt") # sets path

# reads the file
contents = path.read_text()

# Split the contents by newline, remove any empty strings, and convert to integers
grades = [int(grade.strip()) for grade in contents.split('\n') if grade.strip()] # list comprehension for simpleness

# Calculate the sum, average, and count of the grades
total_sum = sum(grades)
count = len(grades)
average = total_sum / count if count else 0  # calculation for mean and checks if there is any grades

# prints the results
print(f"Total Sum: {total_sum}")
print(f"Count of Grades: {count}")
print(f"Average: {average:.2f}") # rounds to 2 decimal places
