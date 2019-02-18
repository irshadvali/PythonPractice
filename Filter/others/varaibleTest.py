x = 1
y = 2
z = 3

a=(x*y)**z/8
print(a)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# Here is how to access the first three items (from first to third):
print(days[0:3])


# Access items from first to fourth:

print(days[0:3])
# ['Mon', 'Tue', 'Wed', 'Thu'] 

# Exactly the same as above
print(days[:4])
# ['Mon', 'Tue', 'Wed', 'Thu'] 

# No boundaries
print(days[:]) 
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] 

# From first to second-to-last
print(days[0:-1])
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

# From first to third-to-last
print(days[:-2])
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

# From third-to-last to second-to-last
print(days[-3:-1])
# ['Fri', 'Sat'] 

# From third-to-last to last
print(days[-3:])
# ['Fri', 'Sat', 'Sun'] 
name = "John"
print(name[2])

name = "John Smith"
print(name[2:4])
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-2])
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-3:-1])
