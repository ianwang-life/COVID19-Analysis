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
character_age = "43.5"
is_male = True               # Use True or False values
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years young.")
character_name = "David"
character_age = "52"
print(character_name + " felt vibrant and healthy;")
print("he refused to accept the fact that he was actually " + character_age + ".")
current_year = 2020                  # This is a number value
print(current_year)
# Working with strings
phrase = "\"Calgary\"\nAlberta"
print(phrase + "\nis homebase")
country = "CanaDa, NorTH AMErica"
print(country.upper())               # Makes string ALL CAPS
print(country.islower())             # Checks lowercase of string and returns a True or False
print(country.upper().isupper())     # Converts to all uppercase, returning a True value
print(len(country))                  # Length function counts number of characters in the string
