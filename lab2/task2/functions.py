import re
from task2.constants import YES, NO, ERROR_INPUT, FOR_FILES

def username_check(username: str):
    while re.findall(FOR_FILES, username):
        print("Incorrect input")
        username = input()
    return username

def yes_no(y_n : str):
    while(True):
        if(y_n == YES):
            return True
        elif (y_n == NO):
            return False
        print(ERROR_INPUT)
        y_n = input()