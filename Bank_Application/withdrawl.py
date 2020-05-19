from getpass import getpass
import json as js
def withdrawl():
        print("Please enter your username and password")
        username = input("Enter your username")
        password = getpass("Enter yout Password")
        with open("first.json","r+") as up:
            data = js.load(up)
            u=data["Name"]
            p=data["Password"]
        if username in u and password in p:
            userid = data["Name"].index(username)
            print("Welcome", username)
            wamount = int(input("Please Enter amount"))
            amt=data['Amount'][userid]
            rb = amt - wamount
            coustmer["Amount"][userid] = rb
            with open("first.json","r+") as f:
                    js.dump(coustmer,f)
            print(f"Available Balance-->{rb}")
        else:
            print("Invalid username and password")
