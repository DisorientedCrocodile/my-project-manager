import json
import os
from pathgetter import filepath, filepath_status, getpath, getstatuses

class InformationGetter():
    def __init__(self, folderpath):
        self.folderpath = getpath()
        self.statusvariants = ["In progress", "Done"]

    def returnlist(self):
        print("return list func")
        return os.listdir(self.folderpath)

    def change_working_dir(self):
        print("change_working_dir func")
        directory = ""
        with open(filepath, "r") as f:
            directory = json.load(f)["path"]
        os.chdir(os.path.abspath(directory))

    def get_last_change_time(self):
        print("get_last_change_time func")
        last_change_time = []
        for folder in self.returnlist():
            last_change_time.append(os.path.getmtime(self.folderpath + '\\' + folder))
        return last_change_time

    def load_statuses(self):
        print("load_statuses func")
        if getstatuses() == "nope":
            to_dump = {}
            for folder in self.returnlist():
                to_dump[folder] = self.statusvariants[0]

            json.dump(to_dump, open(filepath_status, "w"), indent = 4)
        
            return json.load(open(filepath_status, "r"))
        else:
            return getstatuses()
