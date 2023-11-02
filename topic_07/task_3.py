class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'{self.name} {self.grade}'

class StudentData:
    def __init__(self, students):
        self.students = students

    def sort_students(self, column):
        if column == "name":
            sorted_students = sorted(self.students, key=lambda student: student.name)
            print("\nSorted by name\n")
        elif column == "grade":
            sorted_students = sorted(self.students, key=lambda student: student.grade, reverse=True)
            print("\nSorted by grade\n")
        else:
            print("\nYou entered something wrong in the name of the column to be sorted. Please, try again!!!\n")
            return

        for student in sorted_students:
            print(student)

students = [
    Student('Anna', 85),
    Student('Peter', 90),
    Student('Maria', 75),
    Student('Alex', 88),
    Student('Mykola', 67),
    Student('Mike', 60),
    Student('Fred', 82),
    Student('Alisa', 100),
    Student('Winston', 92),
    Student('John', 98)
]

while True:
    column = input("Select the column by which you want to sort information about students(name, grade): ")
    if column == "name" or column == "grade":
        break
    else:
        print("\nYou entered something wrong in the name of the column to be sorted. Please, try again!!!\n")

student_data = StudentData(students)
student_data.sort_students(column)
