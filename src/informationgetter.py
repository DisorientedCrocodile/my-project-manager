import json
import os

basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, "..", "path.json"))

with open(filepath, "r") as f:
    try:
        projectpath = json.load(f)["path"]
    except:
        print("no path yet")

class InformationGetter():
    def __init__(self, folderpath):
        with open(filepath, "r") as f:
            projectpath = json.load(f)["path"]
        self.folderpath = projectpath
        os.chdir(os.path.abspath(self.folderpath))
    
    def confirm(self):
        print("Everything should be working")

    def returnlist(self):
        return os.listdir(self.folderpath)

    def get_last_change_time(self):
        last_change_time = []
        for folder in self.returnlist():
            last_change_time.append(os.path.getmtime(self.folderpath + '\\' + folder))
        print(last_change_time)
        return last_change_time
