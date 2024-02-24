import Post


class User:
    """User class is responsible for creating users that will use the SocialNetwork also - each user in an observer
    which will be updated if needed (get a notification) - will be explained in this class and th POST class.
    to create a user we need to get a name and a password and by creating it we define a few more private
    variables. in this class we added getters and setters methods to the things we wanted to change or use during our
    code"""
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__static_num_posts = 0
        self.__followers_list = []
        self.__notification_list = []
        self.__isConnected = True

    def get_username(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_followers_list(self):
        return self.__followers_list

    def get_is_connected(self):
        return self.__isConnected

    def set_is_connected(self, is_connected):
        self.__isConnected = is_connected  # will change if the user has logged in or out the SocialNetwork

    """in both follow and unfollow methods the user has to be connected to follow or unfollow somebody else.
        if the user isn't already following the self user then add a user to the self's followers list
        and print the action. same way to the unfollow but remove the user from the followers list"""
    def follow(self, user2):
        if self.__isConnected:
            if self not in user2.__followers_list:
                print(self.__name + " started following " + user2.get_username())
                user2.__followers_list.append(self)
            else:
                raise Exception("you already follow " + user2.get_username())
        else:
            raise Exception(self.get_username() + " is disconnected. Please log in to follow " + user2.get_username())

    def unfollow(self, user2):
        # the user has to be connected to follow somebody else
        if self.__isConnected:
            if self in user2.__followers_list:
                print(self.__name + " unfollowed " + user2.get_username())
                user2.__followers_list.remove(self)
            else:
                raise Exception("you are not following " + user2.get_username())
        else:
            raise Exception(self.get_username() + " is disconnected. Please log in to unfollow " + user2.get_username())

    """ this function responsible for creating a new post. a user can create a post only if he is connected.
        in order to create the post the user needs to send which type of post he wants to create.
        here we will use the design pattern - FACTORY (will be explained in the Post class).
        each post the user creates add 1 to the number of posts the user has"""
    def publish_post(self, post_type, *n):
        if self.__isConnected:
            factory = Post.PostFactory()
            post = factory.create_post(self, post_type, *n)
            self.__static_num_posts += 1
            return post
        else:
            raise Exception(self.get_username() + " is disconnected. Please log in to publish a post")

    def __str__(self):  # prints the data of the user when needed
        return (f"User name: {self.__name}, Number of posts: {self.__static_num_posts}, Number of followers: "
                f"{len(self.__followers_list)}")

    """this function is part of the OBSERVER design pattern:
        it is used to send an UPDATE (add a notification) to the relevant OBSERVER when there is a certain "change" in his post
        for example - a like or a comment on the post """
    def update_note(self, new_note):
        self.__notification_list.append(new_note)

    def print_notifications(self):  # prints the notification list of te
        print(f"{self.__name}'s notifications:")
        for note in self.__notification_list:
            print(note)

    """this function is also part of the OBSERVER design pattern:
        it is used to send a notification of a new post to all of the OBSERVERS(followers) of a certain user(the one 
        who created the post"""
    def notify_followers(self, note):
        for user in self.__followers_list:
            user.update_note(note)
