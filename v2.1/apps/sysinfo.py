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
try:
    color_settings = open(r"A:pyOS\os\colorsettings.txt", 'r')
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
version = 'v2'

print(' _______________________________________')
print('|sys info                              |')
print('|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
processor = platform.processor()
architecture = platform.architecture()[0]
system = platform.system()        
model = platform.processor()
match = re.search(r'(i[0-9])-\d{4}', model)
if match:
    cpu_model = match.group(1)
else:
    cpu_model = "Unknown"
    print("|Processor:", processor)
    print("|CPU Model:", cpu_model)
    print("|Architecture:", architecture)
    print("|System:", system)
    print('|Version '+version)
    print("|device name:",socket.gethostname())
    print('|pyOS made by flightyfigment0')
exitcommand = input('close Y/N ')
if exitcommand == 'Y':
    print('bye')