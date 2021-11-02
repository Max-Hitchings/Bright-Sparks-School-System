import json
import sys
import time


class System():
    # This is called when an instance of this class is created
    def __init__(self):
        # Load rules.json into self.rules as a dictonary
        with open("./data/rules.json") as rules:
            self.rules = json.load(rules)

        # Open database.txt
        with open("./data/database.txt", "r") as db:
            # Save the file in a class variable
            self.database = db
            # Split up the text file into students in a 2D array and by commas
            self.student_list = []
            for student in db.read().splitlines():
                self.student_list.append(student.split(','))

        # set class variable to keep track if it is the first run through
        self.first_time = True
        # store each function in a list for easy acsess
        self.option_list = [self.option1, self.option2,
                            self.option3, self.option4, self.option5, self.quit]

    # function to be called when you want to start the menu
    def start(self):
        # prints welcome message and the menu
        print("Welcome to the menu\nYour options are:")
        for key in self.rules["menu_items"]:
            print(self.rules["menu_items"][key])

        # takes in user input and runs the respective function
        user_choice = int(input())
        self.option_list[user_choice-1]()

    # Function that can be called if to restart the menu
    def restart(self):
        print("Operation successful :)\n")
        time.sleep(1)
        if input("again?") not in self.rules["again_inputs"]:
            self.quit()
        else:
            self.start()

    # Function to be called to sort through srudents by ID
    def findStudent(self, student_id):
        for student in self.student_list:
            if student[0] == student_id:
                return student

    # Function to wrine the updated student list back into the DB
    def updateStudents(self):
        with open("./data/database.txt", "w") as self.database:
            for student in self.student_list:
                self.database.write(",".join(student))
                self.database.write("\n")

    def option1(self):
        # Input what student you want to edit
        student_id = input("Enter the student id\n")
        # Find that students data
        student = self.findStudent(student_id)

        # Input the changes to the student
        student[1] = input("What is the new first name?")
        student[2] = input("What is the new second name?")

        for i in range(len(self.student_list)):
            if self.student_list[i][0] == student[0]:
                self.student_list[i] = student

        # Call updateStudents to add changes to the DB
        self.updateStudents()
        # Call restart to give user option to restart the program
        self.restart()

    def option2(self):
        # Input what student you want to edit
        student_id = input("Enter the student id\n")
        # Find that students data
        student = self.findStudent(student_id)
        # Input what subject grade you want to change
        subject = input(
            f"what subject do you want to change? ({student[3]}/{student[5]}/{student[7]})\n")

        # Loop through subjects until you find the subject then ask what the new grade is
        for i in range(len(student)):
            if student[i] == subject:
                student[i+1] = input("What is the new mark?\n")

        # Add the updated student back to class student list
        for x in range(len(self.student_list)):
            if self.student_list[x][0] == student[0]:
                self.student_list[x] = student

        # Call updateStudents to add changes to the DB
        self.updateStudents()
        # Call restart to give user option to restart the program
        self.restart()

    def option3(self):
        print("\nREPORT:\n")

        # Loop through all students and print out all their data in a nice way
        for student in self.student_list:
            print(
                f"Name: {' '.join(student[1:3])}\nID: {student[0]}\nGrades: {': '.join(student[3:5])}, {': '.join(student[5:7])}, {': '.join(student[7:9])}\n")

        # Call restart to give user option to restart the program
        self.restart()

    def option4(self):
        # Create / open totals.txt
        with open("./data/totals.txt", "w") as totals:
            student_averages = []
            # Loop through all students
            for student in self.student_list:
                # Find students total score
                total_score = int(student[4])+int(student[6])+int(student[8])
                # Find students average score
                average_score = round(total_score / 3)
                # Add these scores to a list with the name and student ID
                student_averages.append(
                    [*student[:3], str(total_score), str(average_score)])
                # Write the list into the file we opened
                totals.write((",").join(
                    [*student[:3], str(total_score), str(average_score)]))
                totals.write("\n")

        # Call restart to give user option to restart the program
        self.restart()

    def option5(self):
        pass

    # Function to quit the program
    def quit(self):
        sys.exit("Goodbye!")


# Create a new instance of the class
school_system = System()
# Run the start function
school_system.start()
