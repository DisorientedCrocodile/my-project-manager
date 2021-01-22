from tkinter import (filedialog , Button, W, E, Label, Tk) 
from informationgetter import InformationGetter

root = Tk()

root.title("ProjectManager")
root.geometry("500x500")
root.configure(background="#1abc9c")

root.columnconfigure(0, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(1, weight=1)

projectpath = ""

def getprojectspath_window():
    global projectpath
    projectpath = filedialog.askdirectory()
    with open("./projectfolderpath.txt", "w") as f:
        f.write(projectpath)
    return projectpath

def getprojectspath():
    global projectpath
    with open("./projectfolderpath.txt", "r") as f:
        projectpath = f.readlines()[0]
    return projectpath

if open("./projectfolderpath.txt", "r").readlines() == []:
    projectpath = getprojectspath_window()
    infoget = InformationGetter(projectpath)
    infoget.confirm()
else:
    projectpath = getprojectspath()
    infoget = InformationGetter(projectpath)
    infoget.confirm()

title = Label(text = "ProjectManger", font = ('Comic Sans MS', 15))
title.grid(row = 0, column = 1)

madeby = Label(text = "Made by DisorientedCrocodile", font = ('Comic Sans MS', 15))
madeby.grid(row = 0, column = 0, sticky = W)

version = Label(text = "v0.1.0", font = ('Comic Sans MS', 15))
version.grid(row = 0, column = 2, sticky = E)

choose_path_button = Button(text = "Choose your 'projects' folder path", command = getprojectspath_window)
choose_path_button.grid(row = 1, column = 0)

root.mainloop()