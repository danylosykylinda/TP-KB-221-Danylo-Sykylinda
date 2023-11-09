
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list_students = [
    {"name":"Bob",  "phone":"0631234567", "email":"bob@gmail.com", "group":"CS-221"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "group":"CS-221"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "group":"CS-222"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "group":"CE-221"},
    {"name":"Zaks",  "phone":"0631234567", "email":"zak@gmail.com", "group":"CE-221"}
]

def printAllList():
    for elem in list_students:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + " Email: " + elem["email"] + " Group: " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Pease enter student email: ")
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
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list_students:
        if name == item["name"]:
            deletePosition = list_students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        list_students.pop(deletePosition)
        #del list_students[deletePosition]
    return


def updateElement():
    # implementation done
    global list_students

    name = input("Please enter name to be updated: ")
    name_update = input("Please enter new name for this student: ")
    phone = input("Please enter phone to be updated: ")
    phone_update = input("Please enter new phone for this student: ")
    email_update = input("Please enter new email for this student: ")
    group_update = input("Please enter new group for this student: ")

    found = False

    for d in list_students:
        if d["name"] == name and d["phone"] == phone:
            d["name"] = name_update
            d["phone"] = phone_update
            d["email"] = email_update
            d["group"] = group_update
            found = True
            break
    if found == False:
        print("\n Student is not found!!! Please, try again.\n")

    list_students = sorted(list_students, key=lambda x: x["name"])
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()