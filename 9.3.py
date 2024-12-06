"""
script: CSV student name and grades
action: This code asks for user input to enter a students first and last name and also asking for their scores on 3
exams. When inputted it creates a csv file and stores the input in it.
author: Cesar Ulises Valenzuela
Date: 12/5/2024
"""
import csv


def collect_and_save_grades():
    file_name = 'grades.csv'
    headers = ['First Name', 'Last Name', 'Grade 1', 'Grade 2', 'Grade 3']

    with open(file_name, mode='w', newline='') as csvfile: # opens file and makes sure there are no blank spaces
        csv_writer = csv.writer(csvfile)                    # mode=w puts it into write mode
        csv_writer.writerow(headers) # writes the headers variable onto the file

        while True:
            # asks the user to input the first and last names and gives a sentinel value
            first_name = input("Student's first name ('exit' to stop): ").strip()
            if first_name.lower() == 'exit':
                print("Exiting and saving data.") # tells user program is ending
                break
            last_name = input("Student's last name: ").strip()

            try:
                grades = [
                    int(input(f"Enter score for Exam {i + 1}: ")) # asks for input on exam 1,2 and 3
                    for i in range(3) # iterates over grades inputted
                ]
            except ValueError:
                print("Invalid input! Scores must be numbers. Restarting student entry.\n") # handles exception
                continue

            csv_writer.writerow([first_name, last_name] + grades) # writes the input into the file
            print(f"Added: {first_name} {last_name} - {grades}\n") # tells user what was added

# calls function
collect_and_save_grades()

