import User
import Notification
# from abc import ABC, abstractmethod


class Post:
    def __init__(self, post_type):
        self.user = None
        self.sug_post = post_type

    def like_notify(self, liker):
        if liker != self.user:  # Ensure the user is not liking their own post
            notification = f'Notification to {self.user.name}: {liker.name} liked your post'
            Notification.send_notification(liker, notification)
            self.user.notification_list.append(notification)


class TextPost(Post):
    def __init__(self, post_type, username, text):
        super().__init__(post_type)
        self.user = username
        self.text = text
        print(username, "published a post")
        will_print = f'"{text}"'
        print(will_print)
        print()


class ImagePost(Post):
    def __init__(self, post_type, username, image):
        super().__init__(post_type)
        self.user = username
        self.image = image
        print(username, "posted a picture")
        print()


class SalePost(Post):
    def __init__(self, post_type, username, what, price, place):
        super().__init__(post_type)
        self.user = username
        self.price = price
        # איך לפנות לUSER עצמו ולא רק לשם? אני רוצה להשוות PASSWORD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.what = what
        self.place = place
        self.available = True
        print(username, "posted a product for sale:")
        # print("For sale!", what,", price:", price,", pickup from:", place)
        will_print = f'For sale! {what}, price: {price}, pickup from: {place}'
        print(will_print)
        print()

    def discount(self, percent, password):
        if self.user.get_password() == password and self.available is True:
            self.price = (self.price*(100-percent))/100
            print(f'Discount on {self.user.get_username()} product! the new price is {self.price}')

    def sold(self, password):
        if self.user.get_password() == password and self.available is True:
            print(f"{self.user.get_username()}'s is sold")
            self.available = False



class PostFactory:
    def create_post(self, username, post_type, *n):
        if post_type == "Text":
            return TextPost(post_type, username, n[0])
        elif post_type == "Image":
            return ImagePost(post_type, username, n[0])
        elif post_type == "Sale":
            return SalePost(post_type, username, n[0], n[1], n[2])
        else:
            raise ValueError("Invalid notification type")
