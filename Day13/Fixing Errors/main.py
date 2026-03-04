# Initial code:
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")

# First issue: an indentation after 'if' statement on line 3 is expected
# First fix:
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")

# Second issue: I entered 'ten' instead of '10', and it couldn't be parsed as an integer.
# Second fix, entering a try and except block:
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print("You can drive at age {age}.")

# Third issue: we must have an f string for the age variable.
# Third fix:
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")