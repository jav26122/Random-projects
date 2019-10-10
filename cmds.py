Version = "0.1b"
VersionDesc = [
    ["0.1b", """
    Started this program.
     """]
]





# Commands[
#   CommandName(s)[
#       Description of command,
#       subcommands[
#           Description of subcommand,
#           flags[
#               flag1[
#                   Description of flag,
#                   [default], [other]
#               flag2[
#                   Description of flag,
#                   [default], [other]
#                   
#       last subcommand list index is flags for main command
# cmds[command[subcommands[ flags[ [default, extras] ]]]]

class Command:
    Type = "Command"
    Names = []
    Subs = []
    Flags = []
    Description = "Description of the command"


class Flag:
    Type = "Flag"
    Names = []
    Description = "Description of the flag"
    Parent = -1
    Default = True
    def __init__(self, Parent, Default):
        self.Parent = Parent
        self.Default = Default
    
class SubCommand:
    Type = "SubCommand"
    Names = []
    Flags = []
    Description = "Description of subcommand"
    Parent = -1
    def __init__(self, Parent):
        self.Parent = Parent

Cmds = []


Cmd = Command()
Cmd.Names.append("version")
Cmd.Names.append("v")
Cmd.Description = """
    Prints out the version of the program"""
Sub = SubCommand(Cmd)
Sub.Names.append("description")
Sub.Names.append("d")
Sub.Description = """
    Prints out the description of versions"""
Flg = Flag(Sub, True)
Flg.Names.append("current")
Flg.Description = """
Prints out the current version description"""
Flg.Parent = Sub
Sub.Flags.append(Flg)
Flg = Flag(Sub, False)
Flg.Names.append("previous")
Flg.Description = """
Prints out the previous version description"""
Flg.Parent = Sub
Sub.Flags.append(Flg)
Flg = Flag(Sub, False)
Flg.Names.append("all")
Flg.Description = """
Prints out all version descriptions"""
Flg.Parent = Sub
Sub.Flags.append(Flg)
Cmd.Subs.append(Sub)

Cmds.append(Cmd)

    

def checkValidCmd(input): #This function is only for checking if the first command is valid.
    Input = str(input).lower()
    Find = Input.find(' ')
    if Find != -1: # There's a space after the command
        Input = Input[:Find]

    isValid = False
    Cmd = -1
    for i in Cmds:
        for j in i.Names:
            if Input == j:
                isValid = True
                Cmd = i

    return isValid, Cmd

def checkSubCmd(input):
    Input = str(input).lower()
    Val, Cmd = checkValidCmd(Input)
    if Val:
        Find = Input.find(' ')
        if Find != -1:
            Next = Input.find(' ', Find+1)
            if Next != -1:
                Slice = Input[Find:Next]
            else:
                Slice = Input[Find:]

            if Slice[0] != '-': # It's a subcommand, not a flag
                ""

            



while True:

    currentInput = input()
    currentInput = str(currentInput)
    Val, Cmd = checkValidCmd(currentInput)
    while not Val:
        print("Invalid command. Try again.\n")
        currentInput = input()
        currentInput = str(currentInput)
        Val, Cmd = checkValidCmd(currentInput)
    
    if Cmd.Names[0] == "version":
        print(Version)
        #checkSubCmd(currentInput)

















