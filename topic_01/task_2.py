str = input('Enter text to see variants of formatting: ')

print(f"\nText with 'strip': {str.strip()} \n")
print(f"Text with 'capitalize': {str.capitalize()} \n")
print(f"Text with 'title': {str.title()} \n")
print(f"Text with 'upper': {str.upper()} \n")
print(f"Text with 'lower': {str.lower()} \n")
print(f"Text with 'swapcase': {str.swapcase()} \n")

str_old_words = input("The word or string you want to replace in 'str': ")
str_new_words = input("The word with which the old word or string will be replaced: ")
print(f"Text with word replacement: {str.replace(str_old_words, str_new_words)} \n")

str_for_split = input("Write your favorite fruit separated by a comma? I will separate each name from the string \n")
print(f"List of your favorite fruits: {str_for_split.split(', ')}")
