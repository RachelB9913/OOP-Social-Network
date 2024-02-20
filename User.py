import Post
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def unregister_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, notification):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, notification):
        pass


class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__static_num_posts = 0
        self.__followers_list = []
        self.__notification_list = []

    def get_username(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_num_posts(self):
        return self.__static_num_posts

    def get_num_followers(self):
        return len(self.__followers_list)

    def get_followers_list(self):
        return self.__followers_list

    def follow(self, user2):
        # only if the user isn't already following the self user then add a follower
        if user2 not in self.__followers_list:
            print(self.__name + " started following " + user2.get_username())
            self.__followers_list.append(user2)
            # user2.register_observer(self)

    def unfollow(self, user2):
        print(self.__name + " unfollowed " + user2.get_username())
        self.__followers_list.remove(user2)
        # user2.unregister_observer(self)

    def publish_post(self, post_type, *n):
        factory = Post.PostFactory()
        post = factory.create_post(self.__name, post_type, *n)
        return post

    def update(self, notification):
        self.__notification_list.append(notification)

    def __str__(self):
        return f"User name: {self.__name}, Number of posts: {self.__num_posts} , Number of followers: {len(self.__followers_list)}"

    # def print_notifications(self):
    #     for notification in self.notification_list:
    #         print(notification)
