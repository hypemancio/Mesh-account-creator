import json
import requests
import random
from random import randint
import string

s = requests.Session()
file = open("JDaccount.txt","a+")
num_of_accounts = input("How many accounts?  ")
password_option = input("Type 1 to use password in config.json, type 2 to use random passwords:  ")

headers = {
    'Content-Type': 'application/json',
    'X-API-Key': '1A17CC86AC974C8D9047262E77A825A4',
    'Accept': '*',
    'X-Debug': '1',
    'User-Agent': 'JDSports/5.3.1.207 CFNetwork/808.3 Darwin/16.3.0',
    'Accept-Encoding': 'gzip, deflate',
    'MESH-Commcerce-Channel': 'iphone-app'
}

with open("config.json") as jsons:
    config = json.load(jsons)

email = config['email']

index = config['email'].find("@")
for n in range(0,int(num_of_accounts)):
        if index == -1:
            account = str(randint(100000, 999999)) +"@" + email
            if password_option == "2":
               config['password'] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
            file.writelines(account + "," + config['password'] + "\n")
            config['email'] = account
            req = s.post("https://commerce.mesh.mx/stores/jdsports/customers", headers=headers, json=config)
            if "error" in req.text:
                print(req.text)
            else:
                print(account + "," + config['password'] + "   Created succesfully" )

        elif index == 0:
            account = str(randint(100000, 999999)) + email
            if password_option == "2":
               config['password'] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
            file.writelines(account + "," + config['password'] + "\n")
            config['email'] = account
            req = s.post("https://commerce.mesh.mx/stores/jdsports/customers", headers=headers, json=config)
            if "error" in req.text:
                print(req.text)
            else:
                print(account + "," + config['password'] + "   Created succesfully" )
        else:
            account = email[:index] + "+" + str(randint(100000, 999999)) + email[index:]
            if password_option == "2":
               config['password'] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
            file.writelines(account + "," + config['password'] + "\n")
            config['email'] = account
            req = s.post("https://commerce.mesh.mx/stores/jdsports/customers", headers=headers, json=config)
            if "error" in req.text:
                print(req.text)
            else:
                print(account + "," + config['password'] + "   Created succesfully" )
