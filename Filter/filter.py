address = ["Flat Floor Street", "18", "New York"]
pins = {"Irshad":1234, "Naushad":1111}

print(address[0], address[1])

pin = int(input("Enter your pin: "))

def find_in_file(f):    
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "That fruit is in the list."
    else:
        return "No such fruit found!"
            
if pin in pins.values():
    if(pin ==1234):
        name="Irshad" 
    else: name="Naushad"
        
    fruit = input("Hi "+name+" Please Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!") 
    print("This info can be accessed only by: ")
    for key in pins.keys():
        print(key)