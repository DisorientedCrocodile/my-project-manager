import os
import json
from tkinter import messagebox, filedialog

basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, "path.json"))
filepath_status = os.path.abspath(os.path.join(basepath, "status.json"))

def create_json(path):
    print("creating json at", path)
    with open(path, "x"):
        pass

def getpath():
    print("getpath func")
    try:
        with open(filepath, "r") as f:
            try:
                projectpath = json.load(f)["path"]
                return projectpath
            except json.decoder.JSONDecodeError:
                getprojectspath_window()
    except FileNotFoundError: # if file doesnt exist it creates it and calls the function again
        create_json(filepath)
        getpath()

def getstatuses():
    print("getstatuses func")
    try:
        with open(filepath_status, "r") as f:
            try:    
                statuses = json.load(f)
            except json.decoder.JSONDecodeError:
                statuses = "nope"
            print(statuses)
            return statuses
    except FileNotFoundError: # if file doesnt exist it creates it and calls the function again
        create_json(filepath_status)
        getstatuses()

# asking for 'projects' folder path 
def getprojectspath_window():
    global filepath

    projectpath = filedialog.askdirectory()
    to_dump = {
        "path" : projectpath
    }
    with open(filepath, "w") as f:
        print("PLEASE WRITE STUFF IN IT")
        json.dump(to_dump, f, indent=4)
        messagebox.showinfo(title="Restart", message="Please restart the application")
        return projectpath

# getting 'projects' folder path, if it isnt there we ask for it
def getprojectspath():
    try:
        return getpath()
    except:
        return ""

