from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            print("The social network " + name + " was created!")
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.users = []
            return cls._instance

    def __str__(self):
        temp = self.name + " social network:\n"
        for user in self.users:
            temp += user.__str__()+ "\n"
        return temp

    def sign_up(self, username, password):
        flag = True
        for user in self.users:
            if user.username == username:
                flag = False
        if flag:
            user1 = User(username, password)
            self.users.append(user1)
            return user1
        raise (Exception("The username " + username + " already exists"))

    def log_out(self, username):
        print(username + " disconnected")

        for user in self.users:
            if user.username == username:
                user.update_state(False)

    def log_in(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                user.update_state(True)
                print(username + " connected")
                return
        raise (Exception("no such user with this details"))