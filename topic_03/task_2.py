list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"Result of method 'extend': {list1}")

list1.append(7)
print(f"Result of method 'append': {list1}")

list1.insert(2, 8)
print(f"Result of method 'insert': {list1}")

list1.remove(4)
print(f"Result of method 'remove': {list1}")

list1.clear()
print(f"Result of method 'clear': {list1}")

list3 = [5, 2, 8, 1, 6]
list3.sort()
print(f"Result of method 'sort': {list3}")

list3.reverse()
print(f"Result of method 'reverse': {list3}")

list4 = list3.copy()
print(f"Result of method 'copy': {list4}")

list4.pop()
print(f"Result of method 'pop': {list4}")

count_of_2 = list4.count(2)
print(f"Result of method 'count': {count_of_2}")

index_of_8 = list4.index(8)
print(f"Result of method 'index': {index_of_8}")

min_val = min(list4)
max_val = max(list4)
print(f"Min value in list4: {min_val}, Max value in list4: {max_val}")

length = len(list4)
print(f"Result of method 'len': {length}")
