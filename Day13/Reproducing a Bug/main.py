from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# Error occurs as dice_num is being assigned a value between 1 and 6, rather than 0 and 5.

# Here, I show that the bug is being caused when dic_num is assigned a value of 6.
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 6
print(dice_images[dice_num])

# Fixed version:
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
