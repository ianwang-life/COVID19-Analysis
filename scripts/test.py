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

c = cube(5)
print(str(c) + "\n")

# If Statements
is_male = False     # Set boolean as True or False
is_tall = False      # Set boolean as True or False
if is_male or is_tall:       # can use "or" as well as "and"
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# Use of "and/not/elif"
if is_male and is_tall:
    print("You are a tall man")
elif is_male and not(is_tall):
    print("You are a short man")
elif not(is_male) and is_tall:
    print("You are not a man, but you are tall")
else:
    print("You are neither a man nor tall")

# Exponential Function via For Loop
def raise_to_power(base_num, pow_num):
    res = 1
    for index in range(pow_num):
        res = res * base_num        # base_num * base_num * base_num * ... etc.
    return res

teams = (raise_to_power(2, 5))
print("There are " + str(teams) + " teams in the tournament.")

# Array
rows = 3
cols = 7
A = [[1]*cols for _ in range(rows)]
print(A)
print(3**3)

# 2D Lists and Nested Loops
num_grid = [
[1, 2, 3],     # row 0 with 3 columns
[4, 5, 6],     # row 1 with 3 columns
[7, 8, 9],     # row 2 with 3 columns
[0]            # row 3 with 1 column
]
print(num_grid[0][0])
print(num_grid[2][1])
print(num_grid[3][0])
# Print out every element in a 2D array
for row in num_grid:
    for col in row:
        print(col)

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":               # if letter.lower() in "aeiou"
            if letter.isupper():
                translation = translation + "_Y_"
            else:
                translation = translation + "_y_"
        else:
            translation = translation + letter
    return translation

print(translate("Hello Canada"))     # can replace user's choice: input("Enter a phrase: ")
'''
Multiple-line comments useful for blocking out codes for debugging
but should generally use # for each line
'''
