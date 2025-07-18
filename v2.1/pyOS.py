import keyboard

keyboard.send('F11')

import os
from os import startfile
import datetime
import webbrowser
import time
import datetime
import socket
import platform
import subprocess
import re
import sys
import sysconfig
import ctypes
import random
from datetime import datetime
import requests
import GPUtil
import platform
import psutil
import socket
import os
import shutil
from datetime import timedelta
import time
import GPUtil


def get_uptime():
    boot_time = psutil.boot_time()
    now = time.time()
    uptime_seconds = now - boot_time
    return str(timedelta(seconds=int(uptime_seconds)))

def get_gpu():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if not gpus:
            return "No GPU found"
        return ", ".join([gpu.name for gpu in gpus])
    except Exception as e:
        return f"GPU Error: {str(e)}"

def get_resolution():
    try:
        import screeninfo
        monitors = screeninfo.get_monitors()
        return f"{monitors[0].width}x{monitors[0].height}"
    except:
        return "Unknown"

def get_shell():
    return os.environ.get("ComSpec", "Unknown")
def infomain():
    uname = platform.uname()
    total, used, free = shutil.disk_usage("/")

    
    print(f"{'Hostname:':<15}{socket.gethostname()}")
    print(f"{'OS:':<15}{uname.system} {uname.release}")
    print(f"{'Kernel:':<15}{uname.version}")
    print(f"{'Uptime:':<15}{get_uptime()}")
    print(f"{'CPU:':<15}{platform.processor()}")
    print(f"{'RAM:':<15}{round(psutil.virtual_memory().used / 1024**3, 1)} GB / {round(psutil.virtual_memory().total / 1024**3, 1)} GB")
    print(f"{'GPU:':<15}{get_gpu()}")
    print(f"{'Resolution:':<15}{get_resolution()}")
    print(f"{'Shell:':<15}{get_shell()}")
    print(f"{'Disk Used:':<15}{round(used / 1024**3, 1)} GB / {round(total / 1024**3, 1)} GB")
def get_all_users():
    try:
        with open(r"A:\pyOS\os\users.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def assign_permissions(username):
    # Give admin to first user
    existing_users = get_all_users()
    role = "admin" if len(existing_users) == 0 else "user"
    with open(r"A:\pyOS\os\userpermissions.txt", "a") as f:
        f.write(f"{username}:{role}\n")
    return role

def get_user_role(username):
    try:
        with open(r"A:\pyOS\os\userpermissions.txt", "r") as f:
            for line in f:
                user, role = line.strip().split(":")
                if user == username:
                    return role
    except FileNotFoundError:
        return "user"
    return "user"

def clssetting():
    settings = open(r"A:\pyOS\os\clsonloop.txt", 'r')
    CLEARONLOOP = settings.read()
    settings.close()
    if CLEARONLOOP.strip() == 'Y':
        CLEAR = True
        
    elif CLEARONLOOP.strip() == 'N':
        CLEAR = False
        

def create_folders(parent_dir, folder_names):
    for folder_name in folder_names:
        folder_path = os.path.join(parent_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")


shelp = '''
theentireshrekmoivescript
penis
boobie
a
rr
'''

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code} try typing pokemon _________")



def get_cpu_info():
    cpu_info = {}
    cpu_info['architecture'] = platform.architecture()
    cpu_info['machine'] = platform.machine()
    cpu_info['processor'] = platform.processor()
    cpu_info['system'] = platform.system()
    cpu_info['node'] = platform.node()
    
    
    
    return cpu_info

computer_choices = ['paper','rock','scissors']
money = 100

SM_CXSCREEN = 0
SM_CYSCREEN = 1

logo_1 = r'''OOOOOOOOOO_____OOOOOOOOOOOOOOOO_____OOOOOOOOOOOOOOOOOOO_______OOOOOOOOOOOOOOOOOOO_____OOOOOOOOOO
OOOOOOOOO/\OOOO\OOOOOOOOOOOOOO|\OOOO\OOOOOOOOOOOOOOOOO/::\OOOO\OOOOOOOOOOOOOOOOO/\OOOO\OOOOOOOOO
OOOOOOOO/::\OOOO\OOOOOOOOOOOOO|:\____\OOOOOOOOOOOOOOO/::::\OOOO\OOOOOOOOOOOOOOO/::\OOOO\OOOOOOOO
OOOOOOO/::::\OOOO\OOOOOOOOOOOO|::|OOO|OOOOOOOOOOOOOO/::::::\OOOO\OOOOOOOOOOOOO/::::\OOOO\OOOOOOO
OOOOOO/::::::\OOOO\OOOOOOOOOOO|::|OOO|OOOOOOOOOOOOO/::::::::\OOOO\OOOOOOOOOOO/::::::\OOOO\OOOOOO
OOOOO/:::/\:::\OOOO\OOOOOOOOOO|::|OOO|OOOOOOOOOOOO/:::/~~\:::\OOOO\OOOOOOOOO/:::/\:::\OOOO\OOOOO
OOOO/:::/__\:::\OOOO\OOOOOOOOO|::|OOO|OOOOOOOOOOO/:::/OOOO\:::\OOOO\OOOOOOO/:::/__\:::\OOOO\OOOO
OOO/::::\OOO\:::\OOOO\OOOOOOOO|::|OOO|OOOOOOOOOO/:::/OOOO/O\:::\OOOO\OOOOOO\:::\OOO\:::\OOOO\OOO
OO/::::::\OOO\:::\OOOO\OOOOOOO|::|___|______OOO/:::/____/OOO\:::\____\OOO___\:::\OOO\:::\OOOO\OO
O/:::/\:::\OOO\:::\____\OOOOOO/::::::::\OOOO\O|:::|OOOO|OOOOO|:::|OOOO|O/\OOO\:::\OOO\:::\OOOO\O
/:::/OO\:::\OOO\:::|OOOO|OOOO/::::::::::\____\|:::|____|OOOOO|:::|OOOO|/::\OOO\:::\OOO\:::\____\
\::/OOOO\:::\OO/:::|____|OOO/:::/~~~~/~~OOOOOOO\:::\OOOO\OOO/:::/OOOO/O\:::\OOO\:::\OOO\::/OOOO/
O\/_____/\:::\/:::/OOOO/OOO/:::/OOOO/OOOOOOOOOOO\:::\OOOO\O/:::/OOOO/OOO\:::\OOO\:::\OOO\/____/O
OOOOOOOOOO\::::::/OOOO/OOO/:::/OOOO/OOOOOOOOOOOOO\:::\OOOO/:::/OOOO/OOOOO\:::\OOO\:::\OOOO\OOOOO
OOOOOOOOOOO\::::/OOOO/OOO/:::/OOOO/OOOOOOOOOOOOOOO\:::\__/:::/OOOO/OOOOOOO\:::\OOO\:::\____\OOOO
OOOOOOOOOOOO\::/____/OOOO\::/OOOO/OOOOOOOOOOOOOOOOO\::::::::/OOOO/OOOOOOOOO\:::\OO/:::/OOOO/OOOO
OOOOOOOOOOOOO~~OOOOOOOOOOO\/____/OOOOOOOOOOOOOOOOOOO\::::::/OOOO/OOOOOOOOOOO\:::\/:::/OOOO/OOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\::::/OOOO/OOOOOOOOOOOOO\::::::/OOOO/OOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\::/____/OOOOOOOOOOOOOOO\::::/OOOO/OOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO~~OOOOOOOOOOOOOOOOOOOOOO\::/OOOO/OOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\/____/OOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'''
logo2 = r'''        /\ \ /\ \     /\_\       /\ \         / /\      
       /  \ \\ \ \   / / /      /  \ \       / /  \     
      / /\ \ \\ \ \_/ / /      / /\ \ \     / / /\ \__  
     / / /\ \_\\ \___/ /      / / /\ \ \   / / /\ \___\ 
    / / /_/ / / \ \ \_/      / / /  \ \_\  \ \ \ \/___/ 
   / / /__\/ /   \ \ \      / / /   / / /   \ \ \       
  / / /_____/     \ \ \    / / /   / / /_    \ \ \      
 / / /             \ \ \  / / /___/ / //_/\__/ / /      
/ / /               \ \_\/ / /____\/ / \ \/___/ /       
\/_/                 \/_/\/_________/   \_____\/'''
logo3 = r''' ________  ___    ___ ________  ________      
|\   __  \|\  \  /  /|\   __  \|\   ____\     
\ \  \|\  \ \  \/  / | \  \|\  \ \  \___|_    
 \ \   ____\ \    / / \ \  \\\  \ \_____  \   
  \ \  \___|\/  /  /   \ \  \\\  \|____|\  \  
   \ \__\ __/  / /      \ \_______\____\_\  \ 
    \|__||\___/ /        \|_______|\_________\
         \|___|/                  \|_________|'''


class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]

def get_total_physical_memory():
    mem_status = MEMORYSTATUSEX()
    mem_status.dwLength = ctypes.sizeof(mem_status)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem_status))
    return mem_status.ullTotalPhys / (1024 ** 3)  

total_ram_gb = get_total_physical_memory()



def get_ram_size():
    kernel32 = ctypes.windll.kernel32
    c_ulong = ctypes.c_ulong
    mem_info = ctypes.c_ulonglong(0)
    kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(mem_info))
    return mem_info.value / (1024 ** 3)  

ram_size_gb = get_ram_size()

def print_dir_tree(root, indent=''):
            if not os.path.isdir(root):
                print(f"{root} is not a directory.")
                return

            items = sorted(os.listdir(root))
            for index, item in enumerate(items):
                path = os.path.join(root, item)
                connector = '└── ' if index == len(items) - 1 else '├── '
                print(f"{indent}{connector}{item}")
                if os.path.isdir(path):
                    next_indent = '    ' if index == len(items) - 1 else '│   '
                    print_dir_tree(path, indent + next_indent)


def progress_bar(progress, total, bar_length=25):
    progress = min(progress, total)
    percent = progress / total
    arrow = '▮' * int(round(percent * bar_length) - 1) + '▮'
    spaces = '▯' * (bar_length - len(arrow))
    sys.stdout.write('\r{0} {1}%'.format(arrow + spaces, int(percent * 100)))
    sys.stdout.flush()


try:
    color_settings = open(r"A:\pyOS\os\colorsettings.txt", 'r')
    color = color_settings.read()
    color_settings.close()
    if color.strip() == 'red':
        os.system('color 4')
    elif color.strip() == 'blue':
        os.system('color 1')
    elif color.strip() == 'green':
        os.system('color 2')
    elif color.strip() == ('aqua'):
        os.system('color 3')
    elif color.strip() == ('purple'):
        os.system('color 5')
    elif color.strip() == ('white'):
        os.system('color 7')
    elif color.strip() == ('grey'):
        os.system('color 8')
except FileNotFoundError:
    print('Error: color settings file not found. Default color assumed.')
    os.system('color 7')

version = 'V2.1'


try:
    with open(r"A:\pyOS\os\log.txt", "r") as f1:
        print(f1.read())

    total_lines = sum(1 for line in open(r"A:\pyOS\os\log.txt"))
    for line_number, line in enumerate(open(r"A:\pyOS\os\log.txt"), 1):
        progress_bar(line_number, total_lines)
        time.sleep(0.5)

    print('\nBIOS setup complete')
    print('pyOS ' + version)
    print('_______________________________________')

except FileNotFoundError:
    print("logo not found")


loop = 0
list_commands = r'''
cal - simple calculator  
clear - clears the screen  
color - changes text color  
copytxt - duplicates txt file  
count - counts to set number  
create_folder - creates folder in specifed location  
dirtree - displays all directorys  
displaylogo - displays current logo (reformatted)  
echo - works like count but with words  
edittxt - edits selected txt file  
exit - closes pyOS  
info - tells you device info (reformatted)  
link - opens inputed link  
logo - custom logos (logo1, logo2, reset are different I made logos)  
open - opens inputed app  
playmp4 - play any mp4 in the MP4 folder  
pokemon - pokedex thanks to the pokeapi  
pyos github - takes you to the homepage for the GitHub repository  
readtxt - reads inputed txt file  
reset - deletes all data  
settings - tells you set settings  
shutdown - shuts down computer for Windows  
signout - signs you out  
time - tells you 24 time with seconds  
todo - adds a thingy to your todo list  
todoclear - clears todo list  
todolist - displays todo list  
txt - makes txt file with selected name  

_________________________________________________________________________________________________________
|pyOS V2.1 NEW FEATURES AND UPDATES \^o^/                                                                |
|________________________________________________________________________________________________________|
restart - restarts pyOS
info - tells you device info(reformated)
version - tell you the current version 
listusers - lists username and permissions
updateuser - allows admins to change the permissions of other users and admins
newuser - allows admins to add new users
'''



username = 0
login_status = 0


def help_command():
    print(list_commands)


def check_existing_username(username):
    with open((r"A:\pyOS\os\users.txt"), "r") as file:
        existing_usernames = file.readlines()
        existing_usernames = [name.strip() for name in existing_usernames]
        if username in existing_usernames:
            return True
        else:
            return False


def add_user(username):
    with open((r"A:\pyOS\os\users.txt"), "a") as file:
        file.write(username + "\n")
def is_admin(username):
    try:
        with open(r"A:\pyOS\os\userpermissions.txt", "r") as f:
            for line in f:
                line = line.strip()
                if ":" not in line or not line:
                    continue  
                user, role = line.split(":")
                if user == username:
                    return role == "admin"
    except FileNotFoundError:
        return False
    return False



def main():
    new_username = input("Enter your username: ")
    global globalusername
    globalusername = new_username
    
    
    status = 0
    beans = ("h")
   
    if check_existing_username(new_username):
        print("welcome " + new_username)
    elif new_username == '':
        print('welcome Guest to sign in type logout')
    else:
        newuser_answer = input("would you like this to be a new account (y/n):")
        if newuser_answer.lower() in ['y', 'yes']:
            
            existing_users = get_all_users()
            role = "admin" if len(existing_users) == 0 else "user"
            
            add_user(new_username)

            with open(r"A:\pyOS\os\userpermissions.txt", "a") as f:
                f.write(f"{new_username}:{role}\n")

            print(f"User {new_username} added successfully! Assigned role: {role}")
        else:
            print('no new account added ')
            main()


if __name__ == "__main__":
    username = main()


def login():
    if login_status == (0):
        main
    else:
        print("you are already logged in")





logo_number = 0
loop = True
time.sleep(1.5)
os.system('cls')
print('type help for a list of Commands')
print(globalusername)
while loop == True:
    
   
    print('_______________________________________')
    
    now = datetime.now()

    
    formatted_now = now.strftime("|%d-%m-%Y|\n|%H:%M:%S  |")
    print( formatted_now)
    print('¯¯¯¯¯¯¯¯¯¯¯¯')
    command_line = input('pyOS '+globalusername+r">\ ")
    if command_line == "help" or command_line == "?":
        help_command()
    elif command_line == "signout":
        os.system('cls')
        login_status = 0
        main()
   
    elif command_line.startswith("open"):
        app_name = command_line.split(" ")[-1]
        if app_name == 'notepad':
            os.system("notepad.exe")

        elif app_name == ('browser'):
            os.system("msedge.exe")
        elif app_name == ('taskmanager') or app_name == ("tskmngr"):
            os.system("Taskmgr.exe")
        elif app_name == ('files'):
            os.system("explorer.exe")
        elif app_name == ("word"):
            os.system("Word.lnk")
        elif app_name == ("onenote"):
            os.system("OneNote.exe")
        elif app_name == ("mail") or app_name == ("outlook"):
            os.system("Outlook.lnk")
        else:
            print('not a supported app')
    
    elif command_line == ('time'):
        now = datetime.now()
        formatted_now = now.strftime("%H:%M:%S  ")
        print( formatted_now)
    elif command_line == ('exit'):
        break
    elif command_line == ("cal"):
        
        os.system(r'A:\pyOS\apps\cal.py')
    elif command_line.startswith('color') or command_line.startswith('colour'):
        chosen_color = command_line.split(" ")[-1]
        color = chosen_color
        print(' _______________________________________')
        print('|Color settings                        |')
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        if chosen_color == 'red':
            os.system('color 4')
            color_file = open(r'A:\pyOS\os\colorsettings.txt', 'w')
            color_file.write('red')
            color_file.close()
            print('hello world')
        elif chosen_color == 'blue':
            os.system('color 1')
            color_file = open(r'A:\pyOS\os\colorsettings.txt', 'w')
            color_file.write('blue')
            color_file.close()
            print('hello world')
        elif chosen_color == 'green':
            os.system('color 2')
            color_file = open(r'A:\pyOS\os\colorsettings.txt', 'w')
            color_file.write('green')
            color_file.close()
            print('hello world')
        elif chosen_color == 'aqua':
            os.system('color 3')
            color_file = open(r'A:\pyOS\os\colorsettings.txt', 'w')
            color_file.write('aqua')
            color_file.close()
            print('hello world')
        elif chosen_color == 'purple':
            os.system('color 5')
            color_file = open(r'A:\pyOS\os\colorsettings.txt', 'w')
            color_file.write('purple')
            color_file.close()
            print('hello world')
        elif chosen_color == 'white':
            os.system('color 7')
            color_file = open(r'A:\pyOS\os\colorsettings.txt', 'w')
            color_file.write('white')
            color_file.close()
            print('hello world')
        elif chosen_color == 'grey':
            os.system('color 8')
            color_file = open(r'A:\pyOS\os\colorsettings.txt', 'w')
            color_file.write('grey')
            color_file.close()
            print('hello world')
        else:
            print('Invalid color!')

    elif command_line.startswith('link'):
        link = command_line.split(' ')[-1]
        webbrowser.open(link)
    elif command_line == ('theentireshrekmoivescript'):
        f = open(r"A:\pyOS\os\shrek.txt","r")
        print(f.read())
    elif command_line == ("txt"):
        txtname = input('what do you want to call the new file: ')
        txt = open(str(txtname),"x")
    elif command_line.startswith("edittxt"):
        file = command_line.split(' ')[-1]
        edit = input("what text do you want to add: ")
        f = open(str(file), "a")
        f.write(edit)
        print('edit completed')
        f.close()
    elif command_line == ('readtxt'):
        readtxt = input('which file: ')
        index = readtxt.find(".txt")
        if index != -1:
            read = open(str(readtxt),"r")
            print(read.read())
        else:
            readtxt = (readtxt+'.txt')
            read = open(str(readtxt),"r")
            print(read.read())
    elif command_line.startswith('copytxt'):
        copy = command_line.split(' ')[-1]
        opentxt = open(str(copy),'r')
        new_file = open(str(copy)+' - Copy', 'x')
        copying = new_file.write(opentxt)
        opentxt.close()
        new_file.close()
    elif command_line == ('info') or command_line == 'sysinfo':
        infomain()
        print('pyOS',version,' ')
    elif command_line.startswith("logo"):
        edit = command_line.split(' ')[-1]
        print(' _______________________________________')
        print('|BIOS image editor                     |')
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        if edit == ('reset') or edit == ('default'):
            logo_number = ('logo 0')
            f = open(r'A:\pyOS\oslog.txt', "w")
            f.write(r' _ __  _   _  ___  ___'+'\n')
            f.close()        
            f = open(r'A:\pyOS\oslog.txt', 'a')
            f.write(r"| '_ \| | | |/ _ \/ __|"+'\n')
            f.close()
            f = open(r'A:\pyOS\oslog.txt', 'a')
            f.write(r"| |_) | |_| | (_) \__ \ "+'\n')
            f.close()
            f = open(r'A:\pyOS\oslog.txt', 'a')
            f.write(r"| .__/ \__, |\___/|___/ "+'\n')
            f.close
            f = open(r'A:\pyOS\oslog.txt', 'a')
            f.write(r"| |     __/ | "+'\n')
            f.close()
            f = open(r'A:\pyOS\oslog.txt', 'a')
            f.write(r"|_|    |___/  "+'\n')
            f.close()
        elif edit == ('logo1'):
            f = open(r'A:\pyOS\os\log.txt', "w")
            f.write(logo_1)
            logo_number = ('logo 1')
            print('edit completed')
            f.close()
        elif edit == ('logo2'):
            logo_number = ('logo 2')
            f = open(r'A:\pyOS\os\log.txt', "w")
            f.write(logo2)
            print('edit completed')
            f.close()
        elif edit == ('logo3'):
            f = open(r'A:\pyOS\os\log.txt', "w")
            f.write(logo3)
            print('edit completed')
            f.close()
        #elif edit == ('logo4'):
         #   f = open('log.txt', "w")
          #  f.write(logo4)
           # print('edit completed')
            #f.close()
        elif edit == ('custom'):
            inputed_edit = input('Custom Logo:')
            f = open(r'A:\pyOS\os\log.txt', "w")
            f.write(inputed_edit)
            print('edit completed')
            f.close()
        else:
            print('Not a Valid logo')
    
    elif command_line == ('displaylogo'):
        print(' _______________________________________')
        print('|BIOS image                            |')
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        try:
            with open(r"A:\pyOS\os\log.txt",'r') as f1:
               
                print('_______________________________________')
                f1 = open(r'A:\pyOS\os\log.txt','r')
                print(f1.read())
                
        except FileNotFoundError:
            print(r" _ __  _   _  ___  ___ ")
            print(r"| '_ \| | | |/ _ \/ __|")
            print(r"| |_) | |_| | (_) \__ \ ")
            print(r"| .__/ \__, |\___/|___/")
            print(r"| |     __/ |          ")
            print(r"|_|    |___/          .")
             
    elif command_line == ('settings'):
        print(' _______________________________________')
        print('|Settings                              |')
        print('|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|')
        print('|text color: '+color+'                          |')
        #print('|clsloop: '+str(CLEAR)+'                        |')
        if logo_number == 0:
            print('|logo: defualt                         |')
        else:
            print('|logo: '+edit+'                                |') 
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    elif command_line == ('count'):
        no1 = input('count to: ')
        no3 = ('0')
        loop2 = no1
        while int(no3) <+ int(no1):
            no3 = int(no3) + 1
            number = print(no3)
    elif command_line == ('reset'):
        f = open(r'A:\pyOS\os\users.txt', "w")
        f.write("")
        f.close()
        f = open(r'A:\pyOS\os\colorsettings.txt', "w")
        f.write("")
        f.close()
    elif command_line == 'penis':
        print('8====>')
        print('haha peins')
    elif command_line == 'boobies':
        webbrowser.open('https://en.wikipedia.org/wiki/Breast')
    elif command_line == 'a':
        print('a')
    elif command_line == 'clear' or command_line == 'cls':
        os.system('cls')
    elif command_line.startswith('pokemon'):
        pokemon_name = command_line.split(' ')[-1]
        pokemon_info = get_pokemon_info(pokemon_name)

        if pokemon_info:
            print(f"Name: {pokemon_info["name"].capitalize()}")
            print(f"Id: {pokemon_info["id"]}")
            print(f"Height: {pokemon_info["height"]}")
            print(f"Weight: {pokemon_info["weight"]}")
            #print(f'Move: {pokemon_info["ablity"]}')
    elif command_line == 'shutdown':
        os.system('shutdown /s /t 1')
    elif command_line == 'shelp':
        print(shelp)
    elif command_line == 'todo':
        todo_input = input('⌊')
        f = open('tod.txt', "a")
        f.write('\n')
        f.write(todo_input)
        f.close()
       
    elif command_line == 'todolist':
        try:
            with open(r'A:\pyOS\os\tod.txt', 'r') as todo_file:
                lines = todo_file.readlines()
            print("todo list:")
            for line in lines:
                print(line.strip())
        except FileNotFoundError:
            print("The file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif command_line == 'todoclear':
        f = open(r'A:\pyOS\os\tod.txt', "w")
        f.write('')
        f.close()
    


    elif command_line == 'playmp4':
        mp4 = input('⌊')
        MP4FilePath = os.path.join('A:', 'MP4', mp4)
        os.startfile(MP4FilePath)
    
    elif command_line == 'dirtree':
                 
        script_dir = os.path.dirname(os.path.abspath(__file__))
           
        print_dir_tree(script_dir)
    
    elif command_line == 'create_folder':
        parent_directory = input("Enter the parent directory path: ")
        folder_names_input = input("Enter the folder names separated by commas: ")


        folders = [name.strip() for name in folder_names_input.split(",")]


        create_folders(parent_directory, folders)
 
    elif command_line.startswith('echo'):
        echo = command_line.split(' ')[-1]
        num = command_line.split(' ')[-1]
        echo_loop = True
        while True:
            print('|', echo, '|')
            
    elif command_line == 'rr':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D')
    
    elif command_line == ('clsloop'):
        settings = open(r"A:\pyOS\os\clsonloop.txt", 'w')
        CLS = input('⌊Y or N')
        
        if CLS == ('Y'):
            settings.write(CLS)
        elif color.strip() == 'N':
            settings.write(CLS)
    elif command_line == 'pyos github':
        webbrowser.open('https://github.com/flightyfigment0/pyOS')
    elif command_line == 'bj'or command_line == 'blackjack':
        os.system(r'A:\pyOS\apps\bj.py')
    elif command_line == 'restart':
        startfile(r'A:\pyOS\pyOS.py')
        break
    elif command_line == 'version':
        Beta = True
        if Beta == True:
            print('pyOS', version,'Beta')
        else:
            print('pyOS', version,)
    elif command_line == 'newuser':
        if is_admin(globalusername):
            new_username = input("Enter new username: ")
            if check_existing_username(new_username):
                print("That user already exists.")
            else:
                add_user(new_username)
                with open(r"A:\pyOS\os\userpermissions.txt", "a") as f:
                    f.write(f"{new_username}:user\n")
                print(f"User {new_username} created with role: user")
        else:
            print("Access denied: Admins only.")

    elif command_line == 'updateuser':
        if is_admin(globalusername):
            target_user = input("Enter the username to update: ")
            new_role = input("Enter new role (admin/user): ").lower()
            if new_role not in ['admin', 'user']:
                print("Invalid role.")
            else:
                try:
                    with open(r"A:\pyOS\os\userpermissions.txt", "r") as file:
                        lines = file.readlines()

                    with open(r"A:\pyOS\os\userpermissions.txt", "w") as file:
                        updated = False
                        for line in lines:
                            line = line.strip()
                            if ":" not in line:
                                file.write(line + "\n")
                                continue
                            user, role = line.split(":")
                            if user == target_user:
                                file.write(f"{user}:{new_role}\n")
                                updated = True
                            else:
                                file.write(line + "\n")

                        if not updated:
                            print(f"User '{target_user}' not found.")
                        else:
                            print(f"Updated {target_user}'s role to {new_role}.")

                except FileNotFoundError:
                    print("Permissions file not found.")
        else:
            print("Access denied: Admins only.")

    elif command_line == "listuser" or command_line == 'listusers':
        if is_admin(globalusername):
            print(" _______________________________________")
            print("| Registered Users                      |")
            print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
            try:
                with open(r"A:\pyOS\os\userpermissions.txt", "r") as file:
                    users = file.readlines()
                    if not users:
                        print("| No users found.                      |")
                    else:
                        for line in users:
                            line = line.strip()
                            if ":" in line:
                                user, role = line.split(":")
                                print(f"| {user:<15} - {role:<10}         |")
                            else:
                                print(f"| {line:<15} - [INVALID ENTRY]   |")
            except FileNotFoundError:
                print("| userpermissions.txt not found.       |")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        else:
            print("Access denied: Admins only.")


    else:
        print("not a valid command")
    #if CLEAR == True:
    input('press enter for next command ')
    #time.sleep(1)
    os.system('cls')

