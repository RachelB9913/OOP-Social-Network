import User


class Post:
    def __init__(self, post_type):
        self.sug_post = post_type


class TextPost(Post):
    def __init__(self, post_type, username, text):
        super().__init__(post_type)
        self.text = text
        print(username, "posted a picture")
        print('"',text,'"')
        print()


class ImagePost(Post):
    def __init__(self, post_type, username, image):
        super().__init__(post_type)
        self.image = image
        print(username, "posted a picture")
        print()


class SalePost(Post):
    def __init__(self, post_type, username, what, price, place):
        super().__init__(post_type)
        self.price = price
        self.what = what
        self.place = place
        print(username, "posted a product for sale:")
        print("For sale!", what,", price:", price,", pickup from:", place)
        print()


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
