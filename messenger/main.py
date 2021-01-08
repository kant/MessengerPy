# main file
# Please use multiclasses 
# ~ZaZa

class __main__:
    def __init__(self):
        print('\033[95m' + "Welcome to the MessagePY Client, if you want to enter GUI mode press [ENTER], if you want to keep running in terminal mode, type --terminal.")
        resp = str(input().lower())
        if resp == "--terminal":
            print("Running in Cli Mode")
            #run the StartCli CLASS
        else:
            print("Starting GUI!")
            #run the startWindows CLASS



if __name__ == "__main__":
    __main__()

#python terminal colours (just  so that i can remeber)
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKCYAN = '\033[96m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'