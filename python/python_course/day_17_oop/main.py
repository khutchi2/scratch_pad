# OOP Practice -- Classes
class User:
    def __init__(self, user_id, username):  # "Settable" initial values
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0  # Makes a default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Always need trailing parentheses for initializing an object from a class
user_1 = User("001", "axman13")
print(user_1.id)

user_2 = User("002", "jack")

# Method
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)