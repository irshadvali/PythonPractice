# Sample string
my_string = "hello world"

# capitalize() - Capitalizes the first letter
print("capitalize:", my_string.capitalize())  # "Hello world"

# center(width, char) - Centers the string within a specified width, filling with a character
print("center:", my_string.center(30, "-"))  # "----hello world----"

# count(substring) - Counts occurrences of a substring
print("count 'l':", my_string.count("l"))  # 3

# format() - Formats a string using placeholders
formatted_string = "My name is {} and I am {} years old.".format("Alice", 25)
print("format:", formatted_string)  # "My name is Alice and I am 25 years old."

# index(substring) - Returns the index of the first occurrence of a substring
print("index 'world':", my_string.index("world"))  # 6

# isdigit() - Checks if the string consists only of digits
print("isdigit:", "12345".isdigit())  # True
print("isdigit:", "123a45".isdigit())  # False

# isupper() - Checks if all characters in the string are uppercase
print("isupper:", "HELLO".isupper())  # True
print("isupper:", my_string.isupper())  # False

# istitle() - Checks if the string is in title case (Each word starts with uppercase)
print("istitle:", "Hello World".istitle())  # True
print("istitle:", my_string.istitle())  # False

# strip() - Removes leading and trailing whitespace
print("strip:", "  hello  ".strip())  # "hello"

# swapcase() - Swaps uppercase to lowercase and vice versa
print("swapcase:", "Hello WoRLd".swapcase())  # "hELLO wOrld"
