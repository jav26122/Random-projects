

import os
import shutil
from os import path
from shutil import copyfile
rootDir = os.getcwd()



# This source is given by Dr. French
ConfighSource = """
/*** config.h** ** This header file will be used for all our projects.** See PIC24FJ128GA010 data sheet, CH24 regarding Configuration.**
MACRO commands _CONFIG1 and _CONFIG2 are used.*/



 #include <xc.h>// Generic header file, contains all definitions
// for our PIC24 processor (& others)

_CONFIG1(
    JTAGEN_OFF          // disable JTAG interface 0x3FFF0x3 = 0b0011
    & GCP_OFF           // disable general code protection 0x7FFF0x7 = 0b0111
    & GWRP_OFF          // disable flash write protection 0x7FFF0x7 = 0b0111
    & ICS_PGx2          // ICSP interface (2=default) 0x7FFF0x7 = 0b0111
    & FWDTEN_OFF        // disable watchdog timer 0x7F7F0x7 = 0b0111
)


_CONFIG2(
    IESO_OFF          // two speed start up disabled 0x7FFF0x7 = 0b0111
    & FCKSM_CSDCMD      // disable clock-swithcing/monitor  0xFFBF0xB = 0b1011
    & FNOSC_PRIPLL      // primary oscillator: enable PLL   0xFBFF0xB = 0b1011
    & POSCMOD_XT       // primary oscillator: XT mode      0xFFFD0xD = 0b1101The following is the Header file we will be using for all our projects.A copy will need to be placed in each project folder.  The following:#include “config.h” will be included in each program.19
)
"""

# had issues with os.path.join so made this instead
def fixPaths(Path, toAppend = ''):
    newPath = Path + "\\" + toAppend
    newPath = newPath.replace('\\', '/')
    return newPath
    
def FindConfig(startPath = '.'):
    Root = os.getcwd()
    Found = []
    for dirName, subdirList, fileList in os.walk(startPath):
        if "config.h" in fileList:
            print("Found a config.h in " +dirName)
            Found.append(os.path.join(dirName, "config.h"))

    return Found


if not path.exists("config.h"):
    print("No config.h file in current directory.")
    prompt = input("Create new config.h file for embedded systems lab? (Y / N)")
    if str.lower(str(prompt[0])) == 'y':
        ConfighSource = str.encode(ConfighSource)
        newFile = os.open("config.h", os.O_RDWR | os.O_CREAT)
        written = os.write(newFile, ConfighSource)
        print("\nNew config.h has been written to " + os.getcwd() + " (" + str(written) + " bytes)" + '\n')
    else:
        prompt = input("Search for a config.h file in this directory to use? (Y / N)")
        if str.lower(str(prompt[0])) == 'y':
            foundConfigs = FindConfig()
            if foundConfigs:
                if os.path.join(os.getcwd(), foundConfigs[0]) == os.path.join(os.getcwd(), '.\\'+"config.h"):
                    print("config.h already exists in current directory")
                else:
                    shutil.copy(foundConfigs[0], os.path.join(os.getcwd(), "config.h"))
                    print("Found a config.h file to use.")
            else:
                print("No config.h files exist to use as source.")
                input()
                exit()
        else:
            exit()


os.chdir(rootDir)
configSourcePath = os.getcwd()+"\\config.h"

with os.scandir(rootDir) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_dir():
            newDir = fixPaths(rootDir, entry.name)
            print("     Checking "+entry.name+" for config.h...")

            
            os.chdir(newDir)

            if path.exists("config.h"):
                print("         config.h already exists in"+entry.name)
            else:
                print("             config.h is not in "+entry.name+" and will be added.")
                shutil.copy(configSourcePath, os.getcwd())



input() # pretty much just halt to see results.



