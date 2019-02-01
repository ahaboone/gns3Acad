import subprocess

def checkIPavailability(IPlist):
    for IPAddr in IPlist:
        echo_reply=subprocess.call("ping /n 2 {}".format(IPAddr), stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        if echo_reply == 0:
            print("* {} is reachable :)".format(IPAddr))
            continue

        else:
            print('* {} not reachable :( Check connectivity and try again.'.format(IPAddr))

if __name__ == "__main__":
    checkIPavailability(["10.1.1.1", "192.168.1.1"])
