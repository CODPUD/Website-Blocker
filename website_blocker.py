import time
from datetime import datetime as dt

hostsPath = r"CWindows\System32\drivers\etc\hosts"
redirct="127.0.0.1"

#Here enter a websites to block
websites=["",""]
while 1:
    if dt(dt.now().year, dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,18):
        with open(hostsPath, 'r+') as file:
            content=file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirct+" "+site+'\n')
    else:
        with open(hostsPath, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
                file.truncate()
    time.sleep(1800)