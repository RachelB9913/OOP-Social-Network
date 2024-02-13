# class SocialNetwork:
#
#     def __init__(self):  # an empty constructor for the network
#         self.password = None
#         self.name = None
#
#     def sign_up(self, name, password):  # maybe to put in user?
#         self.name = name
#         self.password = password
import none


class SocialNetwork:  # creates a Singleton
    _name = None
    _instance = None

    def __new__(cls):
        if not cls._instance:  # if SocialNetwork doesn't exist - create one
            cls._instance = super().__new__(cls)

        return cls._instance  # if it exists return the SocialNetwork

    # להחליט מה הבנאי של הרשת אמור לקבל
    def print(self):
        print("The social network " + SocialNetwork._name + " was created!")


class Post:
    def __init__(self, sug, content):
        self.type = sug
        self.content = content
