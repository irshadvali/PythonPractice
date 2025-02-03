# Creating two sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# add() - Adds an element to the set
set1.add(6)
print("add:", set1)  # {1, 2, 3, 4, 5, 6}

# clear() - Removes all elements from the set
set_copy = set1.copy()
set_copy.clear()
print("clear:", set_copy)  # set()

# intersection() - Returns a set with elements common to both sets
print("intersection:", set1.intersection(set2))  # {4, 5, 6}

# copy() - Returns a shallow copy of the set
set_copy = set1.copy()
print("copy:", set_copy)  # {1, 2, 3, 4, 5, 6}

# remove() - Removes an element (raises an error if not found)
set1.remove(6)
print("remove:", set1)  # {1, 2, 3, 4, 5}

# pop() - Removes and returns a random element
popped_element = set1.pop()
print("pop:", popped_element, set1)  # Random element removed

# intersection_update() - Updates the set with elements common to both sets
set1.intersection_update(set2)
print("intersection_update:", set1)  # {4, 5}

# union() - Returns a set containing all unique elements from both sets
set3 = {9, 10}
print("union:", set2.union(set3))  # {4, 5, 6, 7, 8, 9, 10}

# update() - Updates the set with elements from another set
set1.update(set3)
print("update:", set1)  # {4, 5, 9, 10}

# symmetric_difference() - Returns a set with elements in either set but not both
print("symmetric_difference:", set2.symmetric_difference(set3))  # {6, 7, 8, 9, 10}

# symmetric_difference_update() - Updates the set with the symmetric difference
set2.symmetric_difference_update(set3)
print("symmetric_difference_update:", set2)  # {6, 7, 8, 9, 10}
