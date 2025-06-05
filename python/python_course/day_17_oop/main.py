# OOP Practice -- Classes
class User:
    def __init__(self, user_id, username):  # "Settable" initial values
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0  # Makes a default value


# Always need trailing parentheses for initializing an object from a class
user_1 = User("001", "axman13")
print(user_1.id)
