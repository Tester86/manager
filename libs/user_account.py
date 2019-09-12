import os
import sys
from getpass import getpass

# globals

anchor = "C:\\Users\\Usuario\\Database"
first_entry = True
usernames = []
passwords = []
accounts = {}

# globals

# auxilary funcs

def first_time_login():
    global usernames
    global passwords
    global accounts
    print("Welcome, and thank you for using Rubicon Operative System!\n")
    username = input("Choose a username > ")
    password = getpass()
    view_pass_confirm = input("Would you like to check your password? > ")
    if "y" in view_pass_confirm:
        print(f"Password you entered: {password}")
        repeat_pass_confirm = input("Would you like to rewrite your password? > ")
        if "y" in repeat_pass_confirm:
            password = input("Password > ")
        else:
            print("Processing...\n")
    else:
        print(f"Ok then! It's all set now, {username}")
    f = open("usernames.txt", "a")
    f.write(username + "\n")
    f.close()
    f = open("passwords.txt", "a")
    f.write(password)
    f.close()

def start():
    print("hi")

def login():
    global first_entry
    global usernames
    global passwords
    global accounts
    username = input("Username > ")
    password = getpass()
    check_user = False
    check_pass = False
    if username in usernames:
        check_user = True
    if password in passwords:
        check_pass = True
    if check_user and check_pass:
        print(f"Welcome, {username}")
        return True
    else:
        print("Incorrect username or password!\n")
        return False
    

# auxiliary funcs

def setup():
    global usernames
    global passwords
    global accounts
    count = 0
    try:
        os.chdir(anchor)
    except:
        os.mkdir(anchor)
        os.chdir(anchor)
        f = open("usernames.txt", "w")
        f.close()
        f = open("passwords.txt", "w")
        f.close()
        first_time_login()
    finally:
        f = open("usernames.txt", "r")
        content = f.read().split()
        f.close()
        for i in content:
            usernames.append(i)
        f = open("passwords.txt", "r")
        content = f.read().split()
        f.close()
        for i in content:
            passwords.append(i)
        for i in usernames:
            accounts[usernames[count]] = passwords[count]
            count += 1
        if login():
            return True
        else:
            return False
