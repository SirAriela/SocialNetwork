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
        try:
            if (self.username in user.followers) or (self.username == user.username):
                raise Exception("You cannot following yourself or you already follow " + user.username)
            else:
                self.following.append(user)
                user.followers.append(self)
                print(self.username + " started following " + user.username)

        except Exception as e:
            print("there is an error: ", e)

    def unfollow(self, user):
        try:
            if self in user.followers:
                self.following.remove(user)
                user.followers.remove(self)
                print(self.username + " unfollowed " + user.username)

            else:
                raise Exception("you dont follow " + user.username)
        except Exception as e:
            print("there is an error: ", e)

    def publish_post(self, type, *args):
        try:
            if self.state:
                post = PostFactory.create_post(self, type, args)
                print(post)
                self.post.append(post)
                self.notifyFollowers()
                return post
            else:
                raise Exception("cannot make this action. user is not connected")
        except Exception as e:
            print("there is an error: ", e)

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
