# Initial code
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Using print to help resolve the issue, total words displaying as 0
# Before total_words, lets print actual value of inputted variables

print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(total_words)

# Using print we have found that the issue is related to variable: word_per_page.
# All we had to do was change == to = because == is used for comparison, and therefore it was not assigning the new value.

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)