import json
import os

basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, "path.json"))
filepath_status = os.path.abspath(os.path.join(basepath, "status.json"))

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
        self.statusvariants = ["In progress", "Done"]
        os.chdir(os.path.abspath(self.folderpath))

    def returnlist(self):
        return os.listdir(self.folderpath)

    def get_last_change_time(self):
        last_change_time = []
        for folder in self.returnlist():
            last_change_time.append(os.path.getmtime(self.folderpath + '\\' + folder))
        return last_change_time

    def load_statuses(self):
        try:    
            statuses = json.load(open(filepath_status, "r"))
        except json.decoder.JSONDecodeError:
            json.dump({"empty" : True}, open(filepath_status, "w"), indent = 4)
            statuses = json.load(open(filepath_status, "r"))
        
        if statuses == {"empty" : True}:
            to_dump = {}
            for folder in self.returnlist():
                to_dump[folder] = self.statusvariants[0]

            json.dump(to_dump, open(filepath_status, "w"), indent = 4)
        
            return json.load(open(filepath_status, "r"))
        else:
            return statuses
