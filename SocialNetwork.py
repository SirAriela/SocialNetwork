from User import User

class Observer:
    def __init__(self):
        self.state = True

    def updateUserState(self, content):
        self.state = content




class SocialNetwork():
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            print("The social network " + name + " was created!")
            cls._instance = super().__new__(cls);
            cls._instance.name = name
            cls._instance.users = []
            return cls._instance

    def __str__(self):
        temp = self.name + " social network:\n"
        for user in self.users:
            temp += user.__str__()+ "\n"
        return temp

    def sing_up(username, password):
        user1 = User(username, password)

    def logout(self, username):
        print(username + " disconnected")

        for user in self.users:
            if user.name == username:
                user.state(False)

    def log_in(self,username,password):
        for user in self.users:
            if user.name == username:
                user.state(False)