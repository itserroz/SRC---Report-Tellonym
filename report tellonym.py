import requests
import os
import time
#Codded By @404.erroz
hl={
'Host':'api.tellonym.me',
'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
'ContentType':'application/json;charset=utf-8'
}
hx={
'Host': 'api.tellonym.me',
'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Alt-Used': 'tellonym.me:443',
'Connection': 'keep-alive',
'Cookie':'_ga=GA1.2.108215305.1597512944; __gads=ID=e74f10d27a4a2ec5:T=1598138659:S=ALNI_MYBBExqQXb8GTuh6AmNnw9VWYgixA; G_ENABLED_IDPS=google; _gid=GA1.2.1254727696.1598108576; __rtgt_sid=ke6gx1lfqj6m9f',
'Upgrade-Insecure-Requests': '1'
}
usern =[]
url_id= "https://api.tellonym.me/profiles/name/"
urllogin="https://api.tellonym.me/tokens/create"
url_report="https://api.tellonym.me/reports/create"
token=[]
cls= lambda :os.system('cls')
succsess = 0
err=0
stop=0
spamm = 0
hacked=0
fake=0
rate=0
def login(username,password):
    try:
        d = {
            'deviceName': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
            'deviceType': 'web',
            'lang': 'en',
            'captcha': '03AGdBq25_lFdGVNvBoCdEKv2tbXuDctiPorxexi4wuKyYbgz2hSF1rdhE6QBu2-KQ53_-b-nyJIKwXLCz8LL_xp2hQ5WaRU0jcmjxCAbCs-96X1ZfC0JcEd7ZrINjoQwMl6yRGAiLRW6FZUxl3NmnfU8aHwj2fTEGg8D1ZBjYQPnrfGVi1FQX7vvAkLpSGk3y3sriFSUrrjruHEDrdL4pDxJmmYJkVmIJVnhSDjgKGVvLgpTBlcR_vexnv6zvHQX89YGnWcOcp-c-gnqB3eTDaQoV2YVVMu7N2bObkpWQcBhJIG-5UxD5dAgEoI_DHbiNSTkNBrdzfGzPQWwLRHh8HSLNfMtiOEKKBJvufcq8T0G7Yj1FlSmCBGDsGZnekrNf-oF3NioeLrWW',
            'email': username,
            'password': password,
            'limit': '25'
        }
        ss = requests.session()
        req = ss.post(urllogin, data=d, headers=hl)
        if ("accessToken") in req.text:
            x = req.json()["accessToken"]
            token.append(x)
            workz()
        else:
            print("password / username --> incorrect")
            input_login()
    except Exception as z :
        input_login()
def get_id(username,type,slp):
    try:
        ss = requests.session()
        req = ss.get(f"{url_id}{username}", headers=hx)
        user_id = req.json()["id"]
        usern.append(username)
        if type =="1":
            spam(user_id,slp)
        elif type=="2":
            fake_Acc(user_id,slp)
        elif type=="3":
            has_been_hacked(user_id,slp)
        elif type=="4":
            report_all(user_id,slp)
        else:
            print("error try again")
            workz()
    except Exception as w:
            print("Error to get id !")
            usern.remove(username)
            workz()


def spam(user_id,slp):
    global succsess , err
    while stop!=1:

        time.sleep(int(slp))
        try:

            h = {
                'Host': 'api.tellonym.me',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                'ContentType': 'application/json;charset=utf-8',
                'authorization': f'Bearer {token[0]}'
            }
            d = {
                "profileId": user_id,
                "reason": '8',
                "textReason": "",
                "type": '7',
                "limit": '25'
            }
            ss = requests.session()
            req = ss.post(url_report, data=d, headers=h).text
            if req == '"ok"':
                succsess += 1
                print(f"Success : {succsess} | Error : {err}", end="\r")
                check_banned(usern[0])
            elif ("Slow down") in req:
                print("Waiting 5 Minutes .. ")
                slp=300
                err += 1
                print(f"Success : {succsess} | Error : {err}", end="\r")
        except Exception as x :
            err += 1
            print(f"Success : {succsess} | Error : {err}", end="\r")

def fake_Acc(user_id,slp):
    global succsess , err
    while stop!=1:
        time.sleep(int(slp))
        try:
            h = {
                'Host': 'api.tellonym.me',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                'ContentType': 'application/json;charset=utf-8',
                'authorization': f'Bearer {token[0]}'
            }
            d = {
                "profileId": user_id,
                "reason": '9',
                "textReason": "Please Blocking the account ! , is fake !!",
                "type": '7',
                "limit": '25'
            }
            ss = requests.session()
            req = ss.post(url_report, data=d, headers=h).text
            if req == '"ok"':
                succsess += 1
                print(f"Success : {succsess} | Error : {err}", end="\r")
                check_banned(usern[0])
            elif ("Slow down") in req:
                print("Waiting 5 Minutes .. ")
                slp=300
                err += 1
                print(f"Success : {succsess} | Error : {err}", end="\r")
        except Exception as z :
            err += 1
            print(f"Success : {succsess} | Error : {err}", end="\r")
def has_been_hacked(user_id,slp):
    global succsess, err
    while stop!=1:
        time.sleep(int(slp))
        try:
            h = {
                'Host': 'api.tellonym.me',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                'ContentType': 'application/json;charset=utf-8',
                'authorization': f'Bearer {token[0]}'
            }
            d = {
            "profileId": user_id,
            "reason": '10',
            "textReason": "This account has been hacked and the user cannot recover it. Hope you closed!",
            "type": '7',
            "limit": '25'
             }
            ss=requests.session()
            req=ss.post(url_report,data=d,headers=h).text
            if req == '"ok"':
                succsess += 1
                print(f"Success : {succsess} | Error : {err}", end="\r")
                check_banned(usern[0])
            elif ("Slow down") in req:
                print("Waiting 5 Minutes .. ")
                slp = 300
                err += 1
                print(f"Success : {succsess} | Error : {err}", end="\r")
        except Exception as z:
            err += 1
            print(f"Success : {succsess} | Error : {err}", end="\r")
def spam_all(user_id):
    global spamm , err
    try:

            h = {
                'Host': 'api.tellonym.me',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                'ContentType': 'application/json;charset=utf-8',
                'authorization': f'Bearer {token[0]}'
            }
            d = {
                "profileId": user_id,
                "reason": '8',
                "textReason": "",
                "type": '7',
                "limit": '25'
            }
            ss = requests.session()
            req = ss.post(url_report, data=d, headers=h).text
            if req == '"ok"':
                spamm += 1
                check_banned_all(usern[0])
            elif ("Slow down") in req:
                print("Waiting 5 Minutes .. ")
                slp=300
                err += 1
    except Exception as x :
            err += 1
def fake_Acc_all(user_id):
    global fake , err
    try:
            h = {
                'Host': 'api.tellonym.me',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                'ContentType': 'application/json;charset=utf-8',
                'authorization': f'Bearer {token[0]}'
            }
            d = {
                "profileId": user_id,
                "reason": '9',
                "textReason": "Please Blocking the account ! , is fake !!",
                "type": '7',
                "limit": '25'
            }
            ss = requests.session()
            req = ss.post(url_report, data=d, headers=h).text
            if req == '"ok"':
                fake += 1
            elif ("Slow down") in req:
                print("Waiting 5 Minutes .. ")
                slp=300
                err += 1
    except Exception as z :
            err += 1
def has_been_hacked_all(user_id):
    global hacked, err , rate
    try:
            h = {
                'Host': 'api.tellonym.me',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                'ContentType': 'application/json;charset=utf-8',
                'authorization': f'Bearer {token[0]}'
            }
            d = {
            "profileId": user_id,
            "reason": '10',
            "textReason": "This account has been hacked and the user cannot recover it. Hope you closed!",
            "type": '7',
            "limit": '25'
             }
            ss=requests.session()
            req=ss.post(url_report,data=d,headers=h).text
            if req == '"ok"':
                hacked += 1
                print(f"Success Spam : {spamm} - Success Fake Account : {fake} - Success Has been hacked : {hacked} | Error : {err}", end="\r")
            elif ("Slow down") in req:
                print("Waiting 5 Minutes .. ")
                rate +=1
                err += 1
                print(f"Success Spam : {spamm} - Success Fake Account : {fake} - Success Has been hacked : {hacked} | Error : {err}", end="\r")
    except Exception as z:
            err += 1
            print(f"Success Spam : {spamm} - Success Fake Account : {fake} - Success Has been hacked : {hacked} | Error : {err}",end="\r")
def check_banned(username):
    global  stop , cls
    time.sleep(10)
    try:
        ss=requests.session()
        req = ss.get(f"{url_id}{username}", headers=hx).text
        if ("This account is banned.") in req:
            stop += 1
            cls()
            print(4 * f"Closed --> {username}\n")
            input("By @404.erroz")
    except  :
        print("")
def check_banned_all(username):
    global  stop , cls
    time.sleep(10)
    try:
        ss=requests.session()
        req = ss.get(f"{url_id}{username}", headers=hx).text
        if ("This account is banned.") in req:
            stop += 1
            cls()
            print(4 * f"Closed --> {username}\n")
            input("By @404.erroz")
    except  :
        print("")
def report_all(user_id , slp):
    while stop != 1:
        time.sleep(int(slp))
        spam_all(user_id)
        fake_Acc_all(user_id)
        has_been_hacked_all(user_id)
        if rate > 0 :
            slp=350
def workz():
    user = input("Username To Report : ")
    sleep = input("Sleep: ")
    print("""1- Spam \n2- Fake Account \n3- has been hacked\n4- ALL""")
    report_type = input("Enter Number Report : ")
    get_id(user, report_type,sleep)
def input_login():
    u = input("username : ")
    p = input("password : ")
    login(u, p)
input_login()