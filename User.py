from Post import *


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.state = True
        self.followers = []
        self.following = []
        self.post = []
        self.notifications = []

    def update_state(self, state):
        self.state = state

    def follow(self, user):
        self.following.append(user)
        # notify to the other user and add to followers

    def unfollow(self, user):
        self.following.remove(user)
        # notify the other user following list

    def publish_post(self, type, *args):
        post = PostFactory.create_post(self, type, args)
        print(post)
        self.post.append(post)

    # def publish_post(self, type, text, price, location):
    #     post = PostFactory.create_post(self, type, text, price, location)
    #     print(post)
    #     self.post.append(post)

    def __str__(self):
        data = "User name: " + self.username + "," + " Number of posts: " + len(
            self.post) + ", Number of followers: " + len(self.followers)
        return data

    def print_notifications(self):
        for notification in self.notifications:
            print(notification)
