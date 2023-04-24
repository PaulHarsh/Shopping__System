from Storage import StorageFunctions


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        user = StorageFunctions("Users.txt", self.username)
        record = user.retrieve()
        if record:
            record = record.split(',')
            password = record[1]
            if password == self.password:
                return True
        return False




