# Classes should be named using PascalCase, e.g. UserTrainingCompleted
class User:
    pass # allows us to create an empty class without leading to errors

user_1 = User()
user_1.id = "001" #adding attributes to the class
user_1.name = "David" #adding attributes to the class

print(user_1.name)

# Constructors allow us to specify the initial state of an object, we can use def __init__ to define a constructor

class User2:
    def __init__(self, user_id, username): # whenever a new object is being constructed from this class, the two arguments are required
        self.id = user_id
        self.name = username

User2 = User2("004") # I get an error here because I am missing the username
User2 = User2("003", "Jane") # Since defining username and ID in the constructor, I am being prompted for them
print(User2.name) # Jane printed

class InstagramUser:

    def __init__(self, username, user_id): # no need to define followers here, since it is static. I would just have written followers = 0
        self.username = username
        self.id = user_id
        self.followers = 0 # here I have created a followers attribute for the class. It is static

InstagramUser1 = InstagramUser("David", "456")
print(InstagramUser1.followers) # as followers it will always be 0 for each user, unless I change it