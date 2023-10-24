students_data = [
    {'name': 'Anna', 'grade': 85},
    {'name': 'Peter', 'grade': 90},
    {'name': 'Maria', 'grade': 75},
    {'name': 'Alex', 'grade': 88},
    {'name': 'Mykola', 'grade': 67},
    {'name': 'Mike', 'grade': 60},
    {'name': 'Fred', 'grade': 82},
    {'name': 'Alisa', 'grade': 100},
    {'name': 'Winston', 'grade': 92},
    {'name': 'John', 'grade': 98}
]

while True:
    c = input("Select the column by which you want to sort information about students(name, grade): ")
    if c == "name" or c == "grade":
        break
    else:
        print("\nYou entered something wrong in the name of the column to be sorted. Please, try again!!!\n")

def sort_dicts(list, name_col):
    sorted_dict = sorted(list, key=lambda dict: dict[name_col])
    if name_col == "grade":
        print("\nSorted by grade\n")
        sorted_dict.reverse()
        for col in sorted_dict:
            print(f'{col["name"]} {col["grade"]}')
    else:
        print("\nSorted by name\n")
        for col in sorted_dict:
            print(f'{col["name"]} {col["grade"]}')

sort_dicts(students_data, c)
