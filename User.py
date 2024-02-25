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
        user.followers.append(self)
        print(self.username + " started following " + user.username)

    def unfollow(self, user):
        self.following.remove(user)
        user.followers.remove(self)
        print(self.username + " unfollowed " + user.username)

    def publish_post(self, type, *args):
        post = PostFactory.create_post(self, type, args)
        print(post)
        self.post.append(post)
        self.notifyFollowers()
        return post

    # def publish_post(self, type, text, price, location):
    #     post = PostFactory.create_post(self, type, text, price, location)
    #     print(post)
    #     self.post.append(post)

    def __str__(self):
        data = "User name: " + self.username + "," + " Number of posts: " + str(len(
            self.post)) + ", Number of followers: " + str(len(self.followers))
        return data

    def notifyFollowers(self):
        message = f"{self.username} has a new post"
        for user in self.followers:
            user.notifications.append(message)

    def update(self, message, type):
        print(f"notification to {self.username}: {message}")
        self.notifications.append(type)

    def print_notifications(self):
        print(self.username + "'s notifications:")
        for notification in self.notifications:
            print(notification)
