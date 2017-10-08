import time
from datetime import datetime as dt
import platform
import os
import sys
import shutil
import ctypes


def is_first_run():
    if not os.path.exists(os.path.expanduser("~/stay-focused")):
        return True
    else:
        return False


def is_host_file_backed_up():
    if os.path.exists(os.path.abspath("/etc/hosts.sfwb")):
        return True
    else:
        return False


try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
if not is_admin:
    if platform.system() == "Windows":
        print(input("Please \"Run as Administrator\".\nPress any key to quit."))
        quit()
    else:
        print(input("Please run with \"sudo\" command.\nPress any key to quit."))
        quit()

try:
    if sys.argv[1] == "reset":
        shutil.rmtree(os.path.expanduser("~/stay-focused"))
    elif sys.argv[1] == "erase-backup":
        if is_host_file_backed_up():
            os.remove(os.path.abspath("/etc/hosts.sfwb"))
            quit()
except IndexError:
    pass

pathToHostFile = os.path.abspath("C:\Windows\System32\Drivers\etc\hosts") if platform.system() == "Windows" \
    else os.path.abspath("/etc/hosts")
localHost = "127.0.0.1"

if is_first_run():
    if not is_host_file_backed_up():
        if platform.system() == "Windows":
            shutil.copy(os.path.abspath("C:\Windows\System32\Drivers\etc\hosts"),
                        os.path.abspath("C:\Windows\System32\Drivers\etc\hosts.sfwb"))
        else:
            shutil.copy(os.path.abspath("/etc/hosts"), os.path.abspath("/etc/hosts.sfwb"))
    os.mkdir(os.path.expanduser("~/stay-focused"))
    with open(os.path.expanduser("~/stay-focused/TimeTable.txt"), 'w') as timeTable:
        timeTable.write(input("StartTime,EndTime : "))

if os.path.isfile("website-list.txt"):
    with open("website-list.txt", 'r') as siteList:
        listOfWebsitesToBlock = (siteList.read()).split(",")
else:
    input("Could not find \"website-list.txt\" file in the script directory."
          "\nPlease keep the \"website-list.txt\" and \"" + sys.argv[0] + "\" in the same directory."
                                                                          "\nPress any key to quit.")
    quit()

with open(os.path.expanduser("~/stay-focused/TimeTable.txt"), 'r') as timeTable:
    tT = (timeTable.read()).split(",")

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, int(tT[0])) < \
            dt.now() < \
            dt(dt.now().year, dt.now().month, dt.now().day, int(tT[1])):
        #print("Working Hours.")
        with open(pathToHostFile, 'r+') as hostFile:
            content = hostFile.read()
            for website in listOfWebsitesToBlock:
                if website in content:
                    pass
                else:
                    hostFile.write(localHost + " " + website + "\n")
    else:
        #print("Gaming Hours.")
        with open(pathToHostFile, 'r+') as hostFile:
            content = hostFile.readlines()
            hostFile.seek(0)
            for line in content:
                if not any(website in line for website in listOfWebsitesToBlock):
                    hostFile.write(line)
            hostFile.truncate()
    time.sleep(30)
