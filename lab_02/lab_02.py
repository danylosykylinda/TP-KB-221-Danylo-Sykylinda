import csv
import sys

def load_csv(file_name):
    list_students = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_students.append(row)
        print("Data loaded successfully!")
        return list_students
    except FileNotFoundError:
        print("File not found!")


def save_csv(file_name, list_students):
    with open(file_name, 'w', newline='') as file:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in list_students:
            student_data = {
                "name": student["name"],
                "phone": student["phone"],
                "email": student["email"],
                "group": student["group"]
            }
            writer.writerow(student_data)


def printAllList(list_students):
    for elem in list_students:
        strForPrint = "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + ", Email: " + elem["email"] + ", Group: " + elem["group"]
        print(strForPrint)


def addNewElement(list_students):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in list_students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list_students.insert(insertPosition, newItem)
    print("New element has been added")


def deleteElement(list_students):
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list_students:
        if name == item["name"]:
            deletePosition = list_students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        list_students.pop(deletePosition)
        print("Element has been deleted")


def updateElement(list_students):
    name = input("Please enter name to be updated: ")
    name_update = input("Please enter new name for this student: ")
    deletePosition = -1
    for item in list_students:
        if name_update == name == item["name"]:
            phone_update = input("Please enter new phone for this student: ")
            email_update = input("Please enter new email for this student: ")
            group_update = input("Please enter new group for this student: ")
            item["phone"] = phone_update
            item["email"] = email_update
            item["group"] = group_update
            print("Element has been updated")
            deletePosition = -2
            break
        elif name_update != item["name"] and name == item["name"]:
            deletePosition = list_students.index(item)
            if deletePosition == -1:
                print("Student is not found. Please try again correctly.")
            else:
                list_students.pop(deletePosition)
            phone_update = input("Please enter new phone for this student: ")
            email_update = input("Please enter new email for this student: ")
            group_update = input("Please enter new group for this student: ")
            newItem = {"name": name_update, "phone": phone_update, "email": email_update, "group": group_update}
            insertPosition = 0
            for item_up in list_students:
                if name_update > item_up["name"]:
                    insertPosition += 1
                else:
                    break
            list_students.insert(insertPosition, newItem)
            print("Element has been updated")
            break
    if deletePosition == -1:
        print("Student is not found. Please try again correctly.")


def main():
    if len(sys.argv) < 2:
        print("Please provide the file name as a command line argument!")
        return
    data = load_csv(sys.argv[1])
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(data)
                printAllList(data)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(data)
                printAllList(data)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(data)
            case "P" | "p":
                print("List will be printed")
                printAllList(data)
            case "X" | "x":
                save_csv(sys.argv[1], data)
                print("CSV file is rewritten")
                print("Exit()")
                break
            case _:
                print("Wrong chouse")
if __name__ == '__main__':
    main()
    