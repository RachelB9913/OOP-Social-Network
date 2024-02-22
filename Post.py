from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from PIL import Image


class Post(ABC):
    def __init__(self, user, post_type):
        self.user = user
        self.sug_post = post_type

    def like(self, user):
        if user.get_is_connected():
            if user.get_username() != self.user.get_username():  # Ensure the user is not liking their own post
                print(f"notification to {self.user.get_username()}: {user.get_username()} liked your post")
                note = Notification(user.get_username(), "liked your post")
                self.user.add_note(note)
        else:
            raise Exception(user.get_username() + " is disconnected. Please log in and then send a like")

    def comment(self, user, the_comm):
        if user.get_is_connected():
            if user.get_username() != self.user.get_username():
                print(f"notification to {self.user.get_username()}: {user.get_username()} commented on your post: {the_comm}")
                note = Notification(user.get_username(), "commented on your post")
                self.user.add_note(note)
        else:
            raise Exception(user.get_username() + " is disconnected. Please log in and then send a comment")

    @abstractmethod
    def __str__(self):
        pass


class TextPost(Post):
    def __init__(self, post_type, user, text):
        super().__init__(user, post_type)
        self.user = user
        self.text = text
        print(self)

    def __str__(self):
        return f"{self.user.get_username()} published a post:\n\"{self.text}\"\n"


class ImagePost(Post):
    def __init__(self, post_type, user, image):
        super().__init__(user, post_type)
        self.user = user
        self.image = image
        print(self)

    def display(self):
        print("Shows picture")
        image = Image.open(self.image)
        plt.imshow(image)
        plt.axis('off')
        plt.show()

    def __str__(self):
        return f"{self.user.get_username()} posted a picture\n"


class SalePost(Post):
    def __init__(self, post_type, user, what, price, place):
        super().__init__(user, post_type)
        self.user = user
        self.price = price
        self.what = what
        self.place = place
        self.available = True
        print(self)

    def discount(self, percent, password):
        if self.user.get_is_connected():
            if self.user.get_password() is password and self.available:
                self.price = (self.price*(100-percent))/100
                print(f"Discount on {self.user.get_username()} product! the new price is: {self.price}")
            else:
                raise Exception("either the password is incorrect or the item is unavailable - please check")
        else:
            raise Exception(self.user.get_username() + " is disconnected. Please log in and then do the changes")

    def sold(self, password):
        if self.user.get_is_connected():
            if self.user.get_password() == password and self.available:
                print(f"{self.user.get_username()}'s product is sold")
                self.available = False
            else:
                raise Exception("either the password is incorrect or the item is unavailable - please check")
        else:
            raise Exception(self.user.get_username() + " is disconnected. Please log in and then do the changes")

    def __str__(self):
        if self.available:
            sale_sold = "For sale!"
        else:
            sale_sold = "Sold!"
        return (f"{self.user.get_username()} posted a product for sale:\n{sale_sold} {self.what}, price: {self.price}, "
                f"pickup from: {self.place}\n")


class PostFactory:
    def create_post(self, user, post_type, *n):
        if post_type == "Text":
            post = TextPost(post_type, user, n[0])
        elif post_type == "Image":
            post = ImagePost(post_type, user, n[0])
        elif post_type == "Sale":
            post = SalePost(post_type, user, n[0], n[1], n[2])
        else:
            raise ValueError("Invalid notification type")
        note = Notification(user.get_username(), "has a new post")
        user.notify_followers(note)
        return post


class Notification:
    def __init__(self, user, the_note):
        self.who = user  # who sent the notification?
        self.type = the_note  # what kind of notification? - like, comment, new post

    def __str__(self):
        return f"{self.who} {self.type}"


