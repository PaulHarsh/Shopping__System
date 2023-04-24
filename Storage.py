class StorageFunctions:
    def __init__(self, file, data):
        self.file = file
        self.data = data

    def retrieve(self):
        with open(self.file, "r") as myFile:
            for line in myFile:
                if self.data in line:
                    return line
        return False

    def write(self):
        with open(self.file, "a") as myFile:
            myFile.write(self.data)
