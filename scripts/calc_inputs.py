# Getting input from users
print("Multiply Integers")
num1 = input("Enter an integer number: ")
num2 = input("Enter another integer number: ")
ans = int(num1) * int(num2)              # int() = integer number only
print(ans)

print("\nMultiply Any Two Decimal Numbers")
num3 = input("Enter any number: ")
num4 = input("Enter another number: ")
result = float(num3) * float(num4)       # float() = any decimal number
print(result)

print("\nAverage Calculator")
num5 = input("Enter a number: ")
num6 = input("Enter another number: ")
mean = 0.5*(float(num5) + float(num6))       # float() = any decimal number
print(mean)

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
# Building a basic average calculator
# num1 = input("Enter an integer number: ")
# num2 = input("Enter another integer number: ")
# ans = int(num1) + int(num2)           # int() = integer number only
# print(ans)
print("\nFinding the average of the following: ")
num3 = input("Enter any number: ")
num4 = input("Enter another number: ")
average = 0.5*(float(num3) + float(num4))       # float() = any decimal number
print(average)
