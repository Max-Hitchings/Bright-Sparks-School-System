import sys
import json
import time


class System():
    def __init__(self):
        with open("./data/menu_items.json") as menu_items:
            self.menu_items = json.load(menu_items)

        with open("./data/database.txt", "r") as db:
            self.database = db
            self.student_list = []
            for student in db.read().splitlines():
                self.student_list.append(student.split(','))

    def menu(self):
        time.sleep(2)
        print("Welcome to the menu\nYour options are:")
        for key in self.menu_items:
            print(self.menu_items[key])

        options_mapped = [self.option1, self.option2,
                          self.option3, self.option4, self.quit]

        user_choice = int(input())
        options_mapped[user_choice-1]()

    def findStudent(self, student_id):
        for student in self.student_list:
            if student[0] == student_id:
                return student

    def updateStudents(self):
        with open("./data/database.txt", "w") as self.database:
            for student in self.student_list:
                self.database.write(",".join(student))
                self.database.write("\n")

    def option1(self):
        student_id = input("Enter the student id\n")
        print(', '.join(self.findStudent(student_id)))

        self.menu()

    def option2(self):
        student_id = input("Enter the student id\n")
        student = self.findStudent(student_id)
        subject = input(
            f"what subject do you want to change? ({student[3]}/{student[5]}/{student[7]})\n")

        for i in range(len(student)):
            if student[i] == subject:
                student[i+1] = input("What is the new mark?\n")

        for x in range(len(self.student_list)):
            if self.student_list[x][0] == student[0]:
                self.student_list[x] = student

        # self.database.truncate(0)
        with open("./data/database.txt", "w") as self.database:
            for student in self.student_list:
                self.database.write(",".join(student))
                self.database.write("\n")
            # self.database = new_database

        # return student
        self.menu()

    def option3(self):
        print("\nREPORT:\n")
        for student in self.student_list:
            print(
                f"Name: {' '.join(student[1:3])}\nID: {student[0]}\nGrades: {': '.join(student[3:5])}, {': '.join(student[5:7])}, {': '.join(student[7:9])}\n")
        self.menu()

    def option4(self):
        with open("./data/totals.txt", "w") as totals:
            student_averages = []
            for student in self.student_list:
                total_score = int(student[4])+int(student[6])+int(student[8])
                average_score = round(total_score / 3)

                student_averages.append(
                    [*student[:3], str(total_score), str(average_score)])
                totals.write((",").join(
                    [*student[:3], str(total_score), str(average_score)]))
                totals.write("\n")
        self.menu()

    def quit(self):
        sys.exit("Goodbye!")
