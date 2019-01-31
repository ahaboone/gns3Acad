import os
def readIPfile():
    filePath =""
    while not os.path.isfile(filePath):
        filePath = input("Please enter the path to the IP file: ")
    with open(filePath, "r") as myfile:
        ipAddresses = myfile.readlines()
    return ipAddresses

ipaddr = readIPfile()
print(ipaddr)