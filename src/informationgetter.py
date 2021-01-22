import os

with open("./projectfolderpath.txt", "r") as f:
    projectpath = f.readlines()[0]

class InformationGetter():
    def __init__(self, folderpath):
        self.folderpath = projectpath
        os.chdir(os.path.abspath(self.folderpath))
    
    def confirm(self):
        print("pog")