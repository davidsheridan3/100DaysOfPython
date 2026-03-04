import random
import maths

#Initial code
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Added breakpoint to line 9 and stepped over it, in order to see what the new_item variable was.
# Highlighted line is executed next and one just above it has been executed.
# As well as using the step over function, I used the step into function to see what was happening, and then step out to exit the function.
# Step into my code does the exact same thing as step into, but ignores library functions.
# Threads and variables show values of variables in the current scope, and they update as you step through the code.

# As I stepped through the for loop, I noticed that the b_list wasn't being updated and remained empty.
# This is due to the fact that b_list.append was outside the for loop.

# Updated code:
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item) #indented this line
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# Now whenever we loop through, a new item is added to the b_list.