from Login import Login
from Registration import Registration
from Validation import Validation


class Menu:

    @staticmethod
    def interface_login():
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = Login(username, password)
        access = user.login()
        if access:
            print("Access Granted")
        else:
            print("Access Denied")
        Menu.menu()


    @staticmethod
    def interface_registration():
        print(
            "Password MUST have at least:\nlength 8\n1 uppercase character\n1 lowercase character\n1 digit\n1 special character")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = Registration(username, password)
        if not user.check_user_existence():
            print("Username already exists")
        else:
            data = Validation(password)
            if data.confirm_password():
                confirmation_password = input("Enter confirmation password: ")
                if data.confirm(confirmation_password):
                    user.registration()
                    print("User registered successfully")
                else:
                    print("Passwords do not match")
            else:
                print("Password does not match requirements")
        Menu.menu()

    @staticmethod
    def menu():
        print("\nPlease enter one of the following:\nLogin (L)\nRegistration (R)\nExit (E)\n")
        option = input("")
        if option != "L" and option != "R" and option != "E":
            print("Incorrect Option")
            Menu.menu()
        elif option == "L":
            Menu.interface_login()
        elif option == "R":
            Menu.interface_registration()
        else:
            print("Menu exited")
