import requests, os, platform, time
from colorama import Fore, Back, Style

print(Fore.RED + """

    ____                  ___   ____  _      __             
   / __ \____ _____ _____|__ \ / __ \(_)____/ /_  ___  _____
 """ + Fore.GREEN + """ / /_/ / __ `/ __ `/ ___/_/ // /_/ / / ___/ __ \/ _ \/ ___/
 """ + Fore.BLUE + """/ _, _/ /_/ / /_/ (__  ) __// _, _/ / /__/ / / /  __(__  ) 
""" + Fore.RED + """/_/ |_|\__,_/\__, /____/____/_/ |_/_/\___/_/ /_/\___/____/
""" + Fore.BLUE + """            /____/                razgonnaruleitall



""" + Fore.WHITE)

print("Webhook Spammer")
print("")
print("")

user = input("[" + Fore.GREEN + "SYSTEM" + Fore.WHITE + "] What is the username youd like?: ")
webhook = input("[" + Fore.GREEN + "SYSTEM" + Fore.WHITE + "] Please enter the Webhook: ") # input for webhook url
text = input("[" + Fore.GREEN + "SYSTEM" + Fore.WHITE + "] Please enter the Message that should be spammed: ")
everyonespam = input("[" + Fore.GREEN + "SYSTEM" + Fore.WHITE + " ] Would you like to spam @everyone? Y/n: ")

if everyonespam == "Y":
	text += " @everyone"
else:
	pass

if everyonespam == "y":
	text += " @everyone"
else:
	pass
# asks for message

if platform.system() == "Windows": # checking the OS of the device running the tool
    clearcmd = "cls"
else:
    clearcmd = "clear"

os.system(clearcmd)

data = {
    "content": text, # data for webhook as json
    "username": user
}
def send(i):
    res = requests.post(webhook, data=data) # sends data to webhook
    try:
        print(Fore.RED + 'getting ratelimited, waiting ' + str(res.json()["retry_after"]) + 'ms.')
        # response: {'global': False, 'message': 'You are being rate limited.', 'retry_after': 12345)}
        time.sleep(res.json()["retry_after"]/1000)
        res = 'waited ' + Fore.RED + str(res.json()["retry_after"]) + 'ms.'
    except:
        i += 1
        res = "Sent message " + text + " successful, EZ."
    print(Fore.MAGENTA + res + Fore.MAGENTA + ' Amount of messages already sent: ' + Fore.CYAN + str(i)) # message for feedback lol
    return i
i = 0
while True: #loop
   i = send(i)
