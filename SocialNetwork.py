from User import User


class SocialNetwork:  # creates a Singleton
    _name = None
    _instance = None
    all_users = {}  # dictionary

    def __new__(cls, name):
        if cls._instance is None:  # if SocialNetwork doesn't exist - create one
            cls._instance = super().__new__(cls)
            print("The social network", name, "was created!")
        return cls._instance  # if it exists return the SocialNetwork

    def get_name(self):
        return self._name

    def get_all_users(self):
        return self.all_users

    def print(self):
        print(self.get_name() + " social network:")
        for users in self.all_users.values():
            print(self.all_users.values())

    '''sign up function - gets a name and a password - if the password is 4 to 8 characters long
         create the user and add it to the user dictionary of the network'''
    def sign_up(self, username, password):
        new_user = User(username, password)
        if len(password) >= 4 & len(password) <= 8:
            self.all_users[username] = new_user
            return new_user

    def log_out(self, username):  # do I suppose to remove the user from the network?
        print(username + " disconnected")

    def log_in(self, username, password):
        if username in self.all_users:  # is it needed? if yes - change to for?
            print(username + " connected")


# class Post:
#     def __init__(self, sug, content):
#         self.type = sug
#         self.content = content


# אני מגזימה???
