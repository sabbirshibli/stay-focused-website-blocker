# Stay Focused Website Blocker


**Stay Focused Website Blocker** is a CLI python program that can block distracting websites like **Facebook**, **YouTube**, **Reddit** etc during your work hours in order to keep you focused and boost your productivity.

# Prerequisites
* You need to have *"Python 3"* installed on your computer in order to use this script. No third party package is required.

# Download and Installation
* You need to have *"Python 3"* installed on your computer in order to use this script. No third party package is required.

To download the program simply click on the green **Clone or Download** button and **Download ZIP**. You may clone the repo if you want to.
![alt text](https://i.imgur.com/iavZikA.png "Clone or Download this repo")

After downloading the zip extract and there you have it
![alt text](https://i.imgur.com/Fi3QSct.png "Extract the zip")

# How it works

After extracting the zip you'll have following files in the directory
![alt text](https://i.imgur.com/Fi3QSct.png "Extract the zip")
```sfwb.py``` is the main executable. ```website-list.txt``` contains the list of websites to be blocked during working hours.
```website-list.txt``` file looks like this
![alt text](https://i.imgur.com/UT7S3qa.png "Extract the zip")
You can write whatever address in here seperated by a **comma(,)**. sfwb will read through this file on runtime to modify your hosts file.

# Usage

Go to the directory where you have extracted the script and open a terminal/cmd instance in that directory. In case of **Windows** you must run CMS as administrator.

#### Mac/Linux
```sh
$ sudo python3 sfwb.py
```

#### Windows
```sh
C:\sfwb-folder\python sfwb.py
```

If this is the first time you are running sfwb, it'll ask for your working hour
![alt text](https://i.imgur.com/J6VGz74.png "Put in your timetable")
Values are comma(,) separated here. So put your working hour start time and end time as **StartTime,EndTime**. In my country wroking hour is from **8am to 6pm** so I'll input **8,16**. Input has to be given in 24 hours format.
This will be asked only the first time. The timetable will be saved in a file in your home directory.

### In order to reset your time table
#### Mac/Linux
```sh
$ sudo python3 sfwb.py reset
```

#### Windows
```sh
C:\sfwb-folder\python sfwb.py reset
```
### In order to remove all changes made by the script
#### Mac/Linux
```sh
$ sudo python3 sfwb.py erase
```

#### Windows
```sh
C:\sfwb-folder\python sfwb.py erase
```
This command will restore your original hosts file and remove all traces of this program.

---

Feedback: shovik.is.here@gmail.com