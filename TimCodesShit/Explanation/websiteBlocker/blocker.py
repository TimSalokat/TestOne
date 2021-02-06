#only workin on linux at the moment

#Import libraries
import time
from datetime import datetime as dt

#Windows host file path
hostsPath = "/etc/hosts"
redirect="127.0.0.1"
#Add the website you want to block, in this list
websites=["www.youtube.com", "youtube.com", "www.facebook.com", "facebook.com"]

blockingSites = input("Activate add blocker? y/n: ")
if blockingSites == "y":
    print(f"Blocking {websites}")
    
while True:
   #Duration during which, website blocker will work
    if blockingSites == "y":
        with open("/etc/hosts",'r+') as file:
            content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(hostsPath,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
                file.truncate()
    time.sleep(.5)