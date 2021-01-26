from tkinter import (filedialog , Button, W, E, Label, Tk, messagebox) 
from informationgetter import *
from datetime import datetime
import tzlocal
import json

# window creation
root = Tk()
root.title("ProjectManager")
root.configure(background="#1abc9c")

# needed global variables
rownum = 1
local_timezone = tzlocal.get_localzone()
folder_id = 0
label_dict = {}
label_list = []

def change_status(folder_id):
    print("change status func")
    to_dump = infoget.load_statuses()
    folder_list = infoget.returnlist()
    if to_dump[folder_list[folder_id]] == "In progress":
        to_dump[folder_list[folder_id]] = "Done"
    else:
        to_dump[folder_list[folder_id]] = "In progress"
    
    json.dump(to_dump, open(filepath_status, "w"), indent = 4)
    label_list[folder_id].configure(text = to_dump[folder_list[folder_id]])
    label_list[folder_id].update()

if getprojectspath() == "":
    projectpath = getprojectspath_window()
else:
    projectpath = getprojectspath()  

infoget = InformationGetter(projectpath)

title = Label(text = "ProjectManager", font = ('Comic Sans MS', 15))
title.configure(background = "#1abc9c")
title.grid(row = 0, column = 0, columnspan = 2)

version = Label(text = "v0.2.0", font = ('Comic Sans MS', 15))
version.configure(background = "#1abc9c")
version.grid(row = 0, column = 3, sticky = E)

last_change_time = []

for time in infoget.get_last_change_time():
    last_change_time.append(datetime.fromtimestamp(time, local_timezone).strftime('%Y-%m-%d %H:%M:%S'))

while folder_id < len(infoget.returnlist()):
    folder = infoget.returnlist()[folder_id]
    # folder title
    l = Label(text = folder)
    l.configure(background = "#1abc9c", font = ("Comic Sans MS", 13))
    l.grid(row = rownum, column = 0, sticky = W)

    # last change time
    changetime = Label(text = last_change_time[folder_id])
    changetime.configure(background = "#1abc9c", font = ("Comic Sans MS", 13))
    changetime.grid(row = rownum, column = 1, sticky = E, padx = 30)

    # status
    status = Label(text = infoget.load_statuses()[folder])
    status.configure(background = "#1abc9c", font = ("Comic Sans MS", 13))
    status.grid(row = rownum, column = 2, sticky = E, padx = 30)
    label_dict[folder] = status
    label_list.append(status)

    change_status_button = Button(text = "Change Status",  command = lambda folder_id=folder_id: change_status(folder_id))
    change_status_button.configure(background = "#3498db")
    change_status_button.grid(row = rownum, column = 3)

    rownum += 1
    folder_id += 1

choose_path_button = Button(text = "Choose your 'projects' folder path", command = getprojectspath_window)
choose_path_button.configure(background = "#3498db")
choose_path_button.grid(row = rownum, column = 0, sticky = W)

madeby = Label(text = "Made by Disoriented Crocodile")
madeby.configure(background = "#1abc9c", font = ("Comic Sans MS", 13))
madeby.grid(row = rownum, column = 2, sticky = E, columnspan = 2)

root.mainloop()