from getpass import getpass
import json as js
def update_details():
    print("Update your Account Details")
    print("Please enter your username and password")
    username = input()
    password = getpass()
    with open("first.json","r+") as up:
        data = js.load(up)
        u=data["Name"]
        p=data["Password"]
    if username in u and password in p:
        userid = data["Name"].index(username)
        userpassid = data["Password"].index(password)
        print("Welcome", username)
        while True:
            updopt = int(input("Select any option-->\n1.Update Username\n2.Update Password\n3.Update addhar number\n4.Update Pan number\n5.Update mobile number\n6.Exit"))
            if updopt == 1:
                username = input("Enter new Username")
                coustmer["Name"][userid]=username
                print("your username is updated successfully")
            elif updopt == 2:
                password = input("Enter new Password")
                repassword = input("Re-Enter your password")
                if password == repassword:
                    coustmer["Password"][userid]=password
                    print("your password is updated successfully")
            elif updopt == 3:
                print("Update Your Addhar Card Number")
                addharno = int(input("Please enter your 16 digit addhar card number-->"))
                coustmer["Addhar_no"][userid]=addharno
                print("your addhar number is updated successfully")
            elif updopt == 4:
                print("Update Your Pan Card Number")
                panno = input("Enter your pan card number-->")
                coustmer["Pan_no"][userid]=panno
                print("your pan card number is updated successfully")
            elif updopt == 5:
                print("Update Mobile Number")
                mobno = int(input("Enter your mobile number-->"))
                coustmer["Mob_no"][userid]=mobno
                print("your mobile number is updated successfully")
            elif updopt ==6:
                with open("first.json","r+") as f:
                    js.dump(coustmer,f)
                print("Done")
                exit()
                break

            else:
                print("Invalid username and password")
