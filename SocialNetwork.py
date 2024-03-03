from User import User
from Post import Post


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
            temp += user.__str__() + "\n"
        return temp

    def sign_up(self, username, password):
        usarenameFlag = True
        passwordFlag = True
        for user in self.users:
            if user.username == username:
                usarenameFlag = False
            if not (len(user.password) >= 4 and len(user.password) <= 8):
                passwordFlag = False
        if usarenameFlag and passwordFlag:
            user1 = User(username, password)
            self.users.append(user1)
            return user1
        if not usarenameFlag:
            raise (Exception("The username " + username + " already exists"))
        if not passwordFlag:
            raise (Exception("the password is not in the correct format"))

    def log_out(self, username):
        for user in self.users:
            if user.username == username:
                try:
                    if user.state:
                        user.update_state(False)
                        print(username + " disconnected")
                        return
                    else:
                         raise Exception(user.username + " is already disconnected")
                except Exception as e:
                    print("there is an error: ", e)

    def log_in(self, username, password):
        found_user = False
        try:
            for user in self.users:
                if user.username == username and user.password == password:
                    found_user = True
                    if not user.state:
                        user.update_state(True)
                    else:
                        raise Exception(user.username + " is connected already")
                    print(username + " connected")
                    break  # No need to continue searching if user is found

            if not found_user:
                raise Exception("There is no user with these credentials: " + username)

        except Exception as e:
            print("There is an error:", e)
