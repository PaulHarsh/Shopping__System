from Storage import StorageFunctions


class Registration:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_user_existence(self):
        user = StorageFunctions("Users.txt", self.username)
        record = user.retrieve()
        if not record:
            return True
        return False

    def registration(self):
        user = StorageFunctions("Users.txt", self.username + "," + self.password + ",\n")
        user.write()

