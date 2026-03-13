class InstagramUser:

    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user): # new method. Method must always have self as the first argument/parameter
        user.followers += 1 # user we follow goes up by 1
        self.following += 1 # accounts we follow goes up by 1

InstagramUser1 = InstagramUser("David", "456")
InstagramUser2 = InstagramUser("Jane", "789")

InstagramUser1.follow(InstagramUser2)
print(InstagramUser1.following)
print(InstagramUser1.followers)
print(InstagramUser2.followers)
print(InstagramUser2.following)