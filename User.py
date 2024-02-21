import Post, Notification
from abc import ABC, abstractmethod


class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__static_num_posts = 0
        self.__followers_list = []
        self.__notification_list = []
        self.__isConnected = True

    def get_username(self):
        return self.__name

    def add_note(self, new_note):
        self.__notification_list.append(new_note)

    def get_password(self):
        return self.__password

    def get_num_posts(self):
        return self.__static_num_posts

    def get_num_followers(self):
        return len(self.__followers_list)

    def get_followers_list(self):
        return self.__followers_list

    def get_is_connected(self):
        return self.__isConnected

    def set_is_connected(self, is_connected):
        self.__isConnected = is_connected

    def follow(self, user2):
        if self.__isConnected:
            # only if the user isn't already following the self user then add a follower
            if self not in user2.__followers_list:
                print(self.__name + " started following " + user2.get_username())
                user2.__followers_list.append(self)
            else:
                print("you already follow " + user2.get_username())
        else:
            print("you are not connected")

    def unfollow(self, user2):
        if self.__isConnected:
            print(self.__name + " unfollowed " + user2.get_username())
            user2.__followers_list.remove(self)
        else:
            print("you are not connected")

    def publish_post(self, post_type, *n):
        if self.__isConnected:
            factory = Post.PostFactory()
            post = factory.create_post(self, post_type, *n)
            self.__static_num_posts += 1
            return post
        else:
            print("you are not connected")

    def __str__(self):
        return (f"User name: {self.__name}, Number of posts: {self.__static_num_posts}, Number of followers: "
                f"{len(self.__followers_list)}")

    def print_notifications(self):
        print(f"{self.__name}'s notifications:")
        for note in self.__notification_list:
            print(note)

    def notify_followers(self, note):
        for user in self.__followers_list:
            user.add_note(note)
