# main file
# Please use multiclasses 
# ~ZaZa

class __main__:
    def __init__(self):
        print("Welcome to the MessagePY Client, if you want to enter GUI mode press [ENTER], if you want to keep running in terminal mode, type --terminal.")
        resp = str(input().lower())
        if resp == "--terminal":
            print("Running in Cli Mode")
            #run the StartCli CLASS
            open = input()
        else:
            print("Starting GUI!")
            #run the startWindows CLASS



if __name__ == "__main__":
    __main__()

