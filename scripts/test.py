print(pow(8,3))            # this is a comment, does not appear when script is run
# Working with lists
friends = ["Jacob", "Erin", "Blake", 7, False, False, "Oscar", "Toni"]
print(friends[3])       # Recall that first index position is 0, then 1, 2, 3 etc.
print(friends[-1])      # Starts from back of the list, first index at back of list is -1, then -2, -3 etc.
print(friends[0:5])     # Selected a range of index 0 to 2 (not including last index)
friends[1] = "Jake"
print(friends[1])
# List functions
lucky = [17,9,5,7,3,99]
friends.extend(lucky)
friends.append("Gus")      # will always add to the end of the list
friends.insert(1, "Kelly")   # new element added, then everything else pushed to the right
friends.remove(7)            # removes first numeric 7 contained in the list, may be more 7's in rest of list
print(friends)

list = [4,2,5,13,9,23,25]
print(list)
# list.clear()               # should remove entire list, not working here in Atom but works in terminal
list.pop()                   # removes the last element in the list
print(list)
# list2 = list.copy()        # should make a duplicate copy list, not working here in Atom but works in terminal
# print(list2)

print(friends)
print(friends.index("Gus"))
print(friends.count(False))  # counts the number of the stated element (boolean, string, or number)
list.sort()                  # sort works for numbers and alphabetical order for text
print(list)
lucky.reverse()
print(lucky)


# Tuples are immutable or cannot be changed/modified (e.g., coordinates)
# Recall that lists [ ] are mutable and can be changed or modified
coordinates = (4, 5)
# cannot do this and change index element: coordinates[1] = 10     because it returns an error (immutable)
print(coordinates[0])
xy = [(4, 5), (6, 7), (80, 34)]  # A list of tuples
print(xy[2])

# Functions
def say_hi(name, age):           # function with inputs
    print("Introductions:")
    print("Hello " + name + ", you are " + str(age))

print("\nStart")
say_hi("Natalie", 27)            # Calling the actual function
say_hi("Isabelle", 34)           # Calling the actual function
print("End\n")

# Return Statement (boolean, string, array)
def cube(x):
    return pow(x,3)              # Cannot put any more code after the return statement, return breaks function

c = cube(7)
print(c)

# If Statements
