# Creating a sample list
my_list = [1, 2, 3, 4, 5]

# append() - Adds an element to the end of the list
my_list.append(6)
print("append:", my_list)  # [1, 2, 3, 4, 5, 6]

# copy() - Returns a shallow copy of the list
list_copy = my_list.copy()
print("copy:", list_copy)  # [1, 2, 3, 4, 5, 6]

# clear() - Removes all elements from the list
list_copy.clear()
print("clear:", list_copy)  # []

# count() - Returns the number of occurrences of a value
print("count of 3:", my_list.count(3))  # 1

# extend() - Extends the list by appending elements from another iterable
my_list.extend([7, 8, 9])
print("extend:", my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# index() - Returns the index of the first occurrence of a value
print("index of 4:", my_list.index(4))  # 3

# insert() - Inserts an element at a specified position
my_list.insert(2, 10)
print("insert at index 2:", my_list)  # [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# remove() - Removes the first occurrence of a value
my_list.remove(10)
print("remove:", my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# reverse() - Reverses the list in place
my_list.reverse()
print("reverse:", my_list)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# sort() - Sorts the list in ascending order
my_list.sort()
print("sort:", my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
