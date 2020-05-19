from getpass import getpass
import json as js
def bal_enquiry():
    print("Balance Enquiry")
    username = input("Enter your username")
    password = getpass("Enter yout Password")
    with open("first.json","r+") as up:
        data = js.load(up)
        u=data["Name"]
        p=data["Password"]
    if username in u and password in p:
        userid = data["Name"].index(username)
        userpassid = data["Password"].index(password)
        print("Welcome", username)
        tamount=coustmer["Amount"][userid]
        print(tamount)
        print("Available Balance",tamount)
    else:
        print("Invalid username and password")
