dict = {'Ivanenko': 'Ivan', 'Petrenko': 'Petro', 'Sidorova': 'Sidor'}
new_dict = {'Smith': 'John', 'Doe': 'Jane', 'Johnson': 'James'}

dict.update({'Brown': 'Michael', 'Davis': 'David'})
print(f"Result of method 'update': {dict}")

del dict['Ivanenko']
print(f"Result of method 'del': {dict}")

dict.clear()
print(f"Result of method 'clear': {dict}")

keys = new_dict.keys()
print(f"Result of method 'keys': {keys}")

values = new_dict.values()
print(f"Result of method 'values': {values}")

items = new_dict.items()
print(f"Result of method 'items': {items}")
