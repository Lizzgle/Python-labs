import re
class Container:

    def __int__(self, *args):
        self.__container = set()

        try:
            self.__container.update(set(args))
        except Exception:
            print("Error when adding")

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