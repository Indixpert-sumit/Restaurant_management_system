import json
import os

path = r"C:\Restaurant_management_system\\login_info.json"

class Login:
    def __init__(self):
        pass

    def login(self):
        with open(path, "r") as file:
            data = json.load(file)
            dictdata = {}
            name = input('Please Enter Your Name: ') 
            id = int(input('Please Enter Your Registration ID: '))
            address = input('Please Enter Your Address: ')
            dictdata = {
                "name": name,
                "id": id,
                "address": address,
            }
            print('You logged in successfully!')
            data.append(dictdata)
            with open(path, "w") as file:
                json.dump(data, file, indent=4)
            


class Signup:
    def __init__(self):
        pass

    def signup(self):
        with open(path, "r") as file:
            data = json.load(file)
            info = {}
                
            name = input('Please Enter Your Name: ') 
            id = int(input('Please Enter Your Registration ID: '))
            add = input('Please Enter Your Address: ')
            print('You signed up successfully!')
            info = {
                "name": name,
                "id": id,
                "address": add,
            }
            data.append(info)
            with open(path, "w") as file:
                json.dump(data, file, indent=4)


class Option(Login):
    def __init__(self):
        pass

    def option(self):
        print('1 - Staff Login')
        print('2 - Admin Login')
        num = int(input('Please enter your choice: '))
        if num == 1:
            self.login()
        elif num == 2:
            self.login()
        else:
            print('Choose a correct option, please.')
            exit()


class Menu(Signup,Option):
    def __init__(self):
        pass

    def menu(self):
        print('\t\tWelcome To Apna Restaurant')
        print('1 - sign up first')
        print('2 - Login')
        
        choice = int(input('Please Enter Your Choice: '))
        
        if choice == 1:
            self.signup()
            self.option() 
        elif choice == 2:
            self.option() 
        else:
            print('Choose a correct option, please.')
            exit()


info = Menu()
info.menu()
