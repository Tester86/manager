import os, sys
import datetime, time
import winsound
import shutil
from colorama import init, Fore, Style
from libs.mp3 import *
import libs.user_account

# globals

home = os.getcwd()
music_folder = "C:\\Users\\Usuario\\Desktop\\Music"
anchor = "C:\\Users\\Usuario\\Desktop\\ROS"

# auxiliary functions for better functioning and syntax

def colorize(string, color):
        init()
        colorized_text = ""
        if color == "red":
                colorized_text = Fore.RED + string + Fore.RESET
        elif color == "blue":
                colorized_text = Fore.BLUE + string + Fore.RESET
        elif color == "green":
                colorized_text = Fore.GREEN + string + Fore.RESET
        elif color == "yellow":
                colorized_text = Fore.YELLOW + string + Fore.RESET
        else:
                raise Exception(f"Color {color} is not defined")
        return colorized_text


def appscan():
        global anchor
        raw_apps = []
        final_apps = {}
        os.chdir(anchor)
        os.chdir("..")
        for i in os.listdir():
                if i.endswith(".lnk"):
                        raw_apps.append(i)
        for i in raw_apps:
                j = i.replace(".lnk", "")
                j = j.replace(" ", "")
                final_apps.update({j.lower():i})
        os.chdir(anchor)
        return final_apps
        

def play(filename):
        winsound.PlaySound(filename, winsound.SND_FILENAME)


#############

def shut():
    confirm = input("Are you sure you want to shut down your computer? (y / n) > ")
    if confirm == "y" or confirm == "Y":
        os.system("shutdown /s /t 1")
    else:
        print("Aborting operation...\n")

def new_file(filename):
    if os.path.exists(filename):
            print(f"This file already exists: {filename}\n")
            overwrite_confirmation = input("Do you want to overwrite it? (y / n) > ")
            if overwrite_confirmation == "y" or overwrite_confirmation == "Y":
                    os.system("file_overwriter.py")
            else:
                    print("Aborting operation...\n")
    else:
            print(f"Creating file: {filename}...\n")
            try:
                    f = open(filename, "w")
                    f.close()
                    print(f"File created: {filename}")
            except:
                    print(f"Error creating file: {filename}") 

def new_folder(dirname):
    try:
        os.mkdir(dirname)
        print(f"Folder successfully created: {dirname}")
    except:
        print(f"Error while creating folder: {dirname}")

def rmmode(name):
        if os.path.exists(name):
                if os.path.isfile(name):
                        try:
                                os.remove(name)
                                print(f"File removed: {name}")
                        except:
                                print(f"Error while trying to remove file: {name}")
                else:
                        try:
                                shutil.rmtree(name, ignore_errors=True)
                                print(f"DIrectory removed: {name}")
                        except:
                                print(f"Error while trying to remove directory: {name}")  
        else:
                if os.path.isfile(name):
                        print(f"This file does not exist: {name}")
                else:
                        print(f"This folder does not exist: {name}")

def changedir(path):
        global anchor
        if path == "home":
                os.chdir(anchor)
        else:
                os.chdir(path)

def ls():
        folders = []
        files = []
        print("\n")
        for i in os.listdir():
                if os.path.isfile(i):
                        files.append(i)
                else:
                        folders.append(i)
        for i in folders:
                print("    [@] " + colorize(i, "blue"))
        print("\n")
        for i in files:
                print("    [*] " + colorize(i, "green"))
        print("\n")
        del(folders)
        del(files)

def fls():
        print("\n")
        for i in os.listdir():
                if os.path.isfile(i):
                        print("    [*] " + colorize(i, "green"))
        print("\n")

def dir():
        print("\n")
        for i in os.listdir():
                if os.path.isdir(i):
                        print("    [@] " + colorize(i, "blue"))
        print("\n")

def look_for_folders():
    directories = []
    anchor = os.getcwd()
    os.chdir("..")
    all_stuff = os.listdir()
    for i in all_stuff:
        if(os.path.isdir(i)):
            directories.append(i)
    if directories:
        print("\n===== FORMER DIRECTORIES =====\n")
        for i in directories:
            print(i)
        print("\n")
    os.chdir(anchor)
    directories = []
    all_stuff = os.listdir()
    for i in all_stuff:
        if(os.path.isdir(i)):
            directories.append(i)
    if directories:
        print("\n===== LATTER DIRECTORIES =====\n")
        for i in directories:
            print(i)
        print("\n")

def start(filename):
        if os.path.exists(filename):
                print(f"Opening {filename}...")
                try:
                        os.system(filename)
                except:
                        print(f"This file does not exist: {filename}")

def open_file(filename):
    if os.path.exists(filename):
        print(f"Opening file: {filename}...\n")
        print("[1] Read file\n[2] Overwrite file\n[3] Append to file\n")
        option = int(input("Option num > "))
        if option == 1:
                f = open(filename, "r")
                content = f.read()
                print(f"\n===== CONTENT OF {filename} =====\n")
                print(content)
        elif option == 2:
                os.system("file_overwriter.py")
        elif option == 3:
                os.system("file_appender.py")
        else:
                print("\nInvalid input, aborting operation...\n")

def initapp(applist, appname):
        global anchor
        try:
                os.chdir(anchor)
                os.chdir("..")
        except:
                print(f"Fatal error: no directory named \"{anchor}\"")
        try:
                os.system("start " + applist[appname])
        except:
                print(f"Fatal error while opening app: {appname}")
        

def cmusic():
    global music_folder
    global anchor
    try:
            os.chdir(anchor)
    except:
            sys.exit()
    os.system("start manager.py")
    songs = []
    counter = 0
    try:
        os.chdir(music_folder)
    except:
        os.mkdir(music_folder)
        os.chdir(music_folder)
    for i in os.listdir():
        if i.endswith(".mp3") or i.endswith(".wav"):
            counter += 1
            print(str(counter) + ". " + i)
            songs.append(i)
        else:
                print("Non valid format")
    while True:
        cmd = input("Number > ")
        try:
            option = int(cmd)
            if option == 99:
                    break
        except:
            print("Select a number within the range of the list")
        try:
            play(songs[option - 1])
        except:
            print("Select a number within the range of the list")

def song():
        global music_folder
        global anchor
        counter = 0
        songs = []
        try:
                os.chdir(music_folder)
        except:
                os.mkdir(music_folder)
                print("Add some music to your folder first!")
        for i in os.listdir():
                if i.endswith(".mp3") or i.endswith(".wav") or i.endswith(".webm"):
                        if len(i.split()) > 2 or len(i.split()) == 2:
                                complete_name = "".join(i.split())
                                complete_name = complete_name.lower()
                                os.rename(i, complete_name)
                                songs.append(complete_name)
                        else:
                                songs.append(i)
                        counter += 1
                        print(str(counter) + ". " + i)
        while True:
                cmd = input("Number > ")
                try:
                        option = int(cmd)
                        if option == 99:
                                os.chdir(anchor)
                                break
                except:
                        print("Select a number within the range of the list")
                try:
                        os.system("start " + songs[option - 1])
                except:
                        try:
                                os.system("termux-open " + songs[option - 1])
                        except:
                                print("Select a number within the range of the list")

def getTime():
    mday = datetime.datetime.now().timetuple().tm_mday
    yday = datetime.datetime.now().timetuple().tm_yday
    hours = datetime.datetime.now().hour
    minutes = datetime.datetime.now().minute
    print(f"Day of the month: {mday}")
    print(f"Day of the year: {yday}")
    print(f"Time: {hours}:{minutes}")

def help():
        help = """
        cmd:         task:
        
        help                    shows help menu
        shutdown                shuts down device
        mkfile                  creates a new file in current directory
        mkdir                   creates a new director in current directory
        rm                      removes an element from current directory
        ls                      shows all files and folders in current directory
        fls                     shows all files in current directory, excluding folders
        dir                     shows all directories in current directory, excluding files
        cd                      changes directory
        lookup                  looks for directories you can go to (you may have to go back first)
        start                   opens a file of current directory
        open                    opens a file of current directory in terminal
        (*)app                  opens an app of the device
        download                download a music file
        cmusic                  plays a song in the console
        music                   plays a song in Predetermined Media Player
        jimena                  asistenta virtual
        clear                   clears the screen
        exit                    exit ROS
        (*)github upload        upload file to github
        (*)github remove        remove file from github\n"""
        print(help)
        
def main():
    print("\nLoading...\nSystem ready.")
    os.chdir(anchor)
    getTime()

    while True:
        cmd = input(os.getcwd() + "> ")
        if cmd == "help":
                help()
        elif cmd == "shutdown":
                shut()
        elif "mkfile" in cmd:
                try:
                        new_file(cmd.split()[1])
                except:
                        print(f"Error creating file: {cmd.split()[1]}")
        elif "mkdir" in cmd:
                try:
                        new_folder(cmd.split()[1])
                except:
                        print("No file or directory name to remove provided")
        elif "remove" in cmd or "delete" in cmd:
                try:
                        rmmode(cmd.split()[1])
                except:
                        print("No file or directory name to remove provided")
        elif cmd == "ls":
                ls()
        elif cmd == "fls":
                fls()
        elif cmd == "dir":
                dir()
        elif "cd" in cmd: 
                full_name_list = cmd.split()[1::]
                full_name = " ".join(full_name_list)
                if full_name == "":
                        changedir("home")
                else:
                        try:
                                changedir(full_name)
                        except:
                                print(f"This directory does not exist: {full_name}")

        elif cmd == "lookup":
                look_for_folders()
        elif "rename" in cmd:
                cmd_list = cmd.split()
                try:
                        old_name = cmd_list[1]
                        new_name = cmd_list[3]
                        os.rename(old_name, new_name)
                        print(f"{old_name} is now called {new_name}")
                except:
                        print("Error, syntax: rename [old name] as [new name]")
        elif "start" in cmd:
                start(cmd.split()[1])
        elif "open" in cmd:
                open_file(cmd.split()[1])
        elif "app" in cmd:
                applist = appscan()
                if cmd == "app show":
                        for i in applist:
                                print(i)
                else:
                        initapp(applist, cmd.split()[1])
        elif cmd == "cmusic":
                cmusic()
        elif cmd == "music":
                song()
        elif "download" in cmd or "dw" in cmd:
                try:
                        download(cmd.split()[1])
                        print("Done")
                except:
                        print("Done")
                finally:
                        adapt()
        elif "jimena" in cmd:
                os.system("start jimena.py")
        elif cmd == "github upload":
                # code plz
               pass
        elif cmd == "github remove":
                # code plz
                pass
        elif cmd == "clear":
                os.system("clear || @cls")
        elif cmd == "exit": 
                print("\nThank you for using Rubicon Operative System, bye!\n")
                time.sleep(1)
                sys.exit()
        else:
                print("Wrong input")
                help()


if __name__ == "__main__":
        if libs.user_account.setup():
                main()
        else:
                if libs.user_account.setup():
                        main()
                else:
                        sys.exit()
