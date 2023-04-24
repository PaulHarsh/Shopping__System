import string


class Validation:
    def __init__(self, data):
        self.data = data

    def confirm(self, data_to_validate):
        if data_to_validate == self.data:
            return True
        return False

    def confirm_password(self):
        if len(self.data) < 8:
            return False
        upp_counter, low_counter, num_counter, chr_counter = 0, 0, 0, 0
        for element in self.data:
            if element in string.ascii_uppercase:
                upp_counter += 1
            elif element in string.ascii_lowercase:
                low_counter += 1
            elif element in string.digits:
                num_counter += 1
            else:
                chr_counter += 1

        if upp_counter > 0 and low_counter > 0 and num_counter > 0 and chr_counter > 0:
            return True
        return False
