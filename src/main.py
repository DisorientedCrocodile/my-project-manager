from tkinter import (filedialog , Button, W, E, Label, Tk, messagebox) 
from informationgetter import *
from datetime import datetime
import tzlocal
import json

root = Tk()

root.title("ProjectManager")
root.geometry("500x500")
root.configure(background="#1abc9c")

root.columnconfigure(0, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(1, weight=1)

projectpath = ""
rownum = 1
local_timezone = tzlocal.get_localzone()
folder_id = 0
basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, "..", "path.json"))

def getprojectspath_window():
    global projectpath
    global filepath

    projectpath = filedialog.askdirectory()
    to_dump = {
        "path" : projectpath
    }
    with open(filepath, "w") as f:
        json.dump(to_dump, f, indent=4)
        print("debug")
    messagebox.showinfo(title="Restart", message="Please restart the application")
    return projectpath

def getprojectspath():
    global projectpath
    global filepath

    with open(filepath, "r") as f:
        try:
            projectpath = json.load(f)
            return projectpath.get("path")
        except:
            return ""

if getprojectspath() == "":
    projectpath = getprojectspath_window()
    infoget = InformationGetter(projectpath)
    infoget.confirm()
else:
    projectpath = getprojectspath()
    infoget = InformationGetter(projectpath)
    infoget.confirm()

title = Label(text = "ProjectManger", font = ('Comic Sans MS', 15))
title.grid(row = 0, column = 0, columnspan = 2)

version = Label(text = "v0.2.0", font = ('Comic Sans MS', 15))
version.grid(row = 0, column = 2, sticky = E)

for time in infoget.get_last_change_time():
    last_change_time = []
    last_change_time.append(datetime.fromtimestamp(time, local_timezone).strftime('%Y-%m-%d %H:%M:%S'))

for folder in infoget.returnlist():
    l = Label(text = folder)
    l.configure(background = "#1abc9c", font = ("Comic Sans MS", 13))
    l.grid(row = rownum, column = 0, sticky = W)
    changetime = Label(text = last_change_time[folder_id])
    changetime.configure(background = "#1abc9c", font = ("Comic Sans MS", 13))
    changetime.grid(row = rownum, column = 1)
    rownum += 1

choose_path_button = Button(text = "Choose your 'projects' folder path", command = getprojectspath_window)
choose_path_button.grid(row = rownum, column = 0, sticky = W)

root.mainloop()