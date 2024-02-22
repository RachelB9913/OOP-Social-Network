from User import User


class SocialNetwork:  # creates a Singleton
    __name = None
    __instance = None
    all_users = dict()  # dictionary

    def __new__(cls, name):
        if cls.__instance is None:  # if SocialNetwork doesn't exist - create one
            cls.__instance = super().__new__(cls)
            print("The social network", name, "was created!")
        return cls.__instance  # if it exists return the SocialNetwork

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_all_users(self):
        return self.all_users

    def print(self):
        print(self.get_name() + " social network:")
        for users in self.all_users.values():
            print(self.all_users.values())

    '''sign up function - gets a name and a password - if the password is 4 to 8 characters long
         create the user and add it to the user dictionary of the network'''

    def sign_up(self, username, password):
        if username not in self.all_users:
            if 4 <= len(password) <= 8:
                new_user = User(username, password)
                self.all_users[username] = new_user
                new_user.set_is_connected(True)
                return new_user
            else:
                raise Exception("please change the password it is not of the right length")
        else:
            raise Exception("there is already a user with this name - change it and try again")

    def log_out(self, username):
        if username in self.all_users:
            if self.all_users[username].get_is_connected():
                print(username + " disconnected")
                self.all_users[username].set_is_connected(False)
            else:
                raise Exception(username + " is already disconnected")
        else:
            raise Exception("there is no user in the network with the name: " + username)

    def log_in(self, username, password):
        if username in self.all_users:
            if not self.all_users[username].get_is_connected() and password is self.all_users[username].get_password():
                    print(username + " connected")
                    self.all_users[username].set_is_connected(True)
            else:
                raise Exception(username + " is already connected or check the password")
        else:
            raise Exception("there is no user in the network with the name: " + username)

    def __str__(self):
        the_network = f"{self.get_name()} social network:\n"
        for users in self.all_users.keys():
            new_user = self.all_users[users]
            the_user = f"{self.all_users[users].__str__()}\n"
            the_network += the_user
        return the_network
