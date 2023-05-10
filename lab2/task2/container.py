import re
from task2.constants import PATH
class Container:

    def __int__(self, *args):
        self.__container = set()

        try:
            self.__container.update(set(args))
        except Exception:
            print("Error when adding")

    def __str__(self):
        return self.__container.__str__()

    def add(self, *args):
        try:
            self.__container.update(set(args))
        except Exception:
            print("Error when adding")

    def remove(self, elem):
        if elem not in self.__container:
            return

        self.__container.remove(elem)

    def find(self, *args):
        elements = self.__container.intersection(args)

        if not elements:
            return "No such element"

        return elements

    def list(self):
        for elem in self.__container:
            print(elem)

    def grep(self, regex: str):
        result = list()
        try:
            for elem in self.__container:
                if re.fullmatch(regex, elem.__str__()):
                    result.append(elem.__str__())
        except Exception:
            return "Error in the regular expression"

        if not result:
            return "No such element"

        return result

class User:

    def __init__(self):
        self.__users = dict()
        with open(PATH + "users.txt", 'r') as file:
            for user_cont in file.readlines():
                user_cont = user_cont.split()
                self.__users[user_cont[0]] = user_cont[1]

    def __del__(self):
        with open(PATH + "users.txt", 'w') as file:
            for user in self.__users:
                file.write(user + " " + self.__users[user] + "\n")

    def add_user(self, username: str):
        self.__users[username] = PATH + username + "\'sContainer.txt"

    def find_user(self, username: str):
        return self.__users[username]

    def list_users(self):
        print(self.__users)