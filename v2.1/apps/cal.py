import keyboard
import os
keyboard.send('F11')
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


print(' _______________________________________')
print('|Calculator                             |')
print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
cal_input = input("what operation do you want:")
if cal_input == ('add') or cal_input == ('+'):
    varb1 = input("first number: ")
    varb2 = input("second number: ")
    answer = int(varb1) + int(varb2)
    print(answer)
elif cal_input == ('sub') or cal_input == ('-'):
    varb1 = input("first number: ")
    varb2 = input("second number: ")
    answer = int(varb1) - int(varb2)
    print(answer)
elif cal_input == ('multi') or cal_input == ('x'):
    varb1 = input("first number: ")
    varb2 = input("second number: ")
    answer = int(varb1) * int(varb2)
    print(answer)
elif cal_input == ('divde') or cal_input == ('/'):
    varb1 = input("first number: ")
    varb2 = input("second number: ")
    answer = int(varb1) / int(varb2)
    print(answer)
exit_command = input('Y/N ')
if exit_command == 'Y':
    print('')