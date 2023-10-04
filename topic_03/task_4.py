def find_insert_position(sorted_list, new_element):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] < new_element:
            left = mid + 1
        else:
            right = mid - 1

    return left

my_list = ["aa", "ff", "ww"]
new_element = input(f"Enter an element what we want insert in massive {my_list}: ")

insert_position = find_insert_position(my_list, new_element)

my_list.insert(insert_position, new_element)
print(f"The entered element '{new_element}' was inserted at position {insert_position}. Updated list: {my_list}")

