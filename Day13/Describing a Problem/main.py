def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# We have a for loop that iterates from 1 through to 20 (exclusive), and then checks if i is equal to 20. If it is, it prints "You got it".
# 2. When is the function meant to print "You got it"?
# The function is meant to print "You got it" when i is equal to 20.
# 3. What are your assumptions about the value of i?
# I assume that i is an integer from 1 to 20, excluding 20, and therefore it will never = 20, which means we will never print "You got it".
