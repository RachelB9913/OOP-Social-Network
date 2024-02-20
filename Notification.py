import User
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


class Notification(ABC):
    def __init__(self, sender):
        self.type = None
        self.sender = sender
        self.receiver = None
        self.followers = sender.get_followers_list()
        self.text = None

    def register_observer(self, user):
        self.followers.append(user)

    def unregister_observer(self, user):
        self.followers.remove(user)

    def send_notification(self, user, text):
        user.receive_notification(text)

    def like_notify(self, user):
        self.text = f'notification to {self.receiver}: {user.get_username()} liked your post'
        self.send_notification(self.text)  # sends a notification to the user
        user.notification_list.append(self.text)

    def comment_notify(self, user, the_comm):
        self.text = f'notification to {self.receiver}: {user.get_username()} commented on your post: {the_comm}'
        self.send_notification(self.text)
        user.notification_list.append(self.text)

    def new_post_notify(self, user):
        self.text = f'{user.get_username()} has a new post'
        self.send_notification(self.text)
        user.notification_list.append(self.text)
