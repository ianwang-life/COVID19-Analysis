print("Hello World")

def insult(victim, verb, noun):
    print("Hey {0}! You {1} like a {2}".format(victim, verb, noun))

insult("there", "code", "monkey")

# This is a comment, does not appear as output when running script
#Drawing a shape
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")
# Variables and Data Types
character_name = "Noah"      # this is a string, storing plain text between quotation marks
character_age = "34.5"
is_male = True               # Use True or False values
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years young.")
character_name = "David"
character_age = 52
print(character_name + " felt vibrant and healthy;")
print("he refused to accept the fact that he was actually " + str(character_age) + ".")
current_year = 2020                  # This is a number value
print(str(current_year) + " was a character-building year!")
# Working with strings
phrase = "\"Calgary\"\nAlberta"
print(phrase + "\nis homebase")
country = "CanaDa, NorTH AMErica"
print(country.upper())               # Makes string ALL CAPS
print(country.islower())             # Checks lowercase of string and returns a True or False
print(country.upper().isupper())     # Converts to all uppercase, returning a True value
print(len(country))                  # Length function counts number of characters in the string
print(phrase[0] + phrase[1] + phrase[2] + phrase[3] + phrase[4])
print("OTTAWA,ON".index("T"))        # Index function passes a parameter to a numeric placement
airport = "YYC"
print(airport.replace("YYC", "YYZ")) # Replaces the name of airport
print(airport + " International Airport")
# Working with numbers
from math import *
print((78/1.35)+(100-2))
print(20 % 3)                        # Mod: first number divide by second number, gives the reminder left
license = -123456
print(abs(license))                  # Absolute values
print("Here is my license number: " + str(abs(license)))
print(pow(2,5))                      # First number to the power of second number
print(max(license,current_year))     # Higher value of the two
print(min(character_age,25))         # Lower value of the two
print(round(3.7))                    # Round numbers to closest integer
print(floor(3.7))                    # Removes decimals so lowest integer is left
print(ceil(3.14))                    # Removes decimals rounding up to highest integer
a = sqrt(36)*exp(-0.05)              # squareroot and exponential
b = log(2)*1e6                       # log = natural logarithm and e = times 10^(value)
c = log10(2)                         # base10 logarithm
d = erf(1)  # Error function at x, used to compute traditional statistical functions such as the cumulative standard normal distribution
e = tan(pi/4)*sin(pi/6)*cos(pi/3)
f = degrees(pi/2)                    # turns radians into degrees
g = radians(60)                      # turns degrees into radians
h = factorial(5)                     # returns the factorial of inserted value
print(h)
