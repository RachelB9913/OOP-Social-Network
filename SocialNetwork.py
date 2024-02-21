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

    def __init__(self, name):
        self._name = name

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
            new_user.set_is_connected(True)
            return new_user

    def log_out(self, username):
        for users in self.all_users.keys():
            if users is username:
                new_user = self.all_users[username]
                print(username + " disconnected")
                new_user.set_is_connected(False)

    def log_in(self, username, password):
        for users in self.all_users.keys():
            if users is username and password is self.all_users[username].get_password():
                new_user = self.all_users[username]
                print(username + " connected")
                new_user.set_is_connected(True)

    def __str__(self):
        the_network = f"{self.get_name()} social network:\n"
        for users in self.all_users.keys():
            new_user = self.all_users[users]
            the_user = f"{self.all_users[users].__str__()}\n"
            the_network += the_user
        return the_network
