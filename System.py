import sys


class System():
    def __init__(self):
        with open("./data/database.txt", "r") as db:
            self.database = db
            self.student_list = []
            for student in db.read().splitlines():
                self.student_list.append(student.split(','))

    def findStudent(self, student_id):
        for student in self.student_list:
            if student[0] == student_id:
                return student

    def option1(self, student_id):
        return ', '.join(self.findStudent(student_id))

    def option2(self, student_id):
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

    def option3(self):
        print("\nREPORT:\n")
        for student in self.student_list:
            print(",".join(student))
        print("\n")

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

    def quit(self):
        sys.exit("Goodbye!")
