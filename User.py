import Post


class User:
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self.static_num_posts = 0
        self.followers_list = []
        self.notification_list = []

    def get_username(self):
        return self._name

    def get_num_posts(self):
        return self.static_num_posts

    def get_num_followers(self):
        return len(self.followers_list)

    def follow(self, user2):
        # only if the user isn't already following the self user then add a follower
        if user2 not in self.followers_list:
            print(self._name + " started following " + user2.get_username())
            self.followers_list.append(user2)

    def unfollow(self, user2):
        print(self._name + " unfollowed " + user2.get_username())
        self.followers_list.remove(user2)

    def publish_post(self, post_type, *n):
        factory = Post.PostFactory()
        post = factory.create_post(self._name, post_type, *n)
        return post




    def __str__(self):
        return f"User name: {self._name}, Number of posts: {self._num_posts} , Number of followers: {len(self.followers_list)}"

    # def print_notifications(self):
    #     for notification in self.notification_list:
    #         print(notification)
