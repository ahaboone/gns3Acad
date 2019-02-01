import sys
def checkIPvalidity(IPAddrList):
    for IPAddr in IPAddrList:
        if (IPAddr.rstrip("\n").split(".")[0] == "127"):
            print("Bad IP")
            sys.exit()
        else:
            print("Good IP")
if __name__ == "__main__":
    checkIPvalidity(["10.1.1.1","192.168.1.1"])
