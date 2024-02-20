import User

# change!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Notification:
    def __init__(self, sug):
        self._type = sug


class LikeNotification(Notification):
    def __init__(self, user):
        super().__init__(user)
        self._type = "Like"

    def print_notifications(self):
        print(self._the_user.get_username() + "liked your post")


class CommentNotification(Notification):
    def __init__(self, user):
        super().__init__(user)
        self._type = "Comment"

    def print_notifications(self):
        print(self._the_user.get_username() + "commented on your post")


class NewPostNotification(Notification):
    def __init__(self, user):
        super().__init__(user)
        self._type = "New Post"

    def print_notifications(self):
        print(self._the_user.get_username() + "has a new post")


# ואז אם משהו עשה לייק או תגובה או פרסם פוסט להוסיף בפונקציה שייצור את הנוטיפיקיישן המתאים ולהוסיף לליסט של ההתראות
# למשתמש שצריך
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type, user):
        if notification_type == "Like":
            return LikeNotification(user)
        elif notification_type == "Comment":
            return CommentNotification(user)
        elif notification_type == "New Post":
            return NewPostNotification(user)
        else:
            raise ValueError("Invalid notification type")
