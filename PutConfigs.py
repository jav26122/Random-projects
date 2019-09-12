

import os
import shutil
from os import path




configSourcePath = os.getcwd()+"\\config.h"
rootDir = os.getcwd()
with os.scandir(rootDir) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_dir():
            newDir = rootDir+"\\"+entry.name
            newDir = newDir.replace('\\', '/')
            print("     Checking "+entry.name+" for config.h...")

            
            os.chdir(newDir)

            if path.exists("config.h"):
                print("         config.h already exists in"+entry.name)
            else:
                print("             config.h is not in "+entry.name+" and will be added.")
                shutil.copy(configSourcePath, os.getcwd())



input()



"""

Was trying to do this shit with os.walk but turns out its easier with os.scandir

for dirName, subdirList, fileList in os.walk(rootDir):
    print('First directory:'+ dirName)
    configSourcePath = os.getcwd()+"\\config.h"
    for x in subdirList:
        print("Found directory: " + x)
        appendPath = "\\"+x
        appendPath = os.getcwd() + appendPath    #This is the directory we need to change to
        print("Current directory:"+os.getcwd())

        os.chdir(appendPath)

        print("New current directory: "+os.getcwd())


        if path.exists("config.h"):
            print("config.h is already in "+x)
        else:
            print("config.h is not in "+x+" and will be added.")
            shutil.copy(configSourcePath, os.getcwd())

    break

"""