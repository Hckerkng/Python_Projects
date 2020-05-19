import json as js
from getpass import getpass
coustmer = {"Name":[],
             "DOB":[],
            "Addhar_no":[],
            "Pan_no":[],
            "Mob_no":[],
            "Password":[],
            "Account_no":[],
            "Amount":[],
            }
a = []
with open("first.json","r+") as up:
    data = js.load(up)
    coustmer.update(data)
def create_account():
    print("Create an Account")
    copt = int(input("Select any option-->\n1.Current Account\n2.Saving Account"))
    def printWellOrdered(number, x, k):
        if (k == 0):
            d ='1000'+str(number)
            a.append(d)
        for i in range( (x + 1), 10):
            printWellOrdered(number * 10 + i, i, k - 1)
    def generateWellOrdered(k):
        printWellOrdered(0, 0, k)
#    if __name__ == "__main__":
    k = 4
    generateWellOrdered(k)
    if copt == 1:
        print("Open Current Account")
        username = input("Please enter your name--->")
        coustmer["Name"].append(username)
        dob = input("Enter your date of birth")
        coustmer["DOB"].append(dob)
        addharno = int(input("Please enter your 16 digit addhar card number-->"))
        coustmer["Addhar_no"].append(addharno)
        panno = input("Enter your pan card number--->")
        coustmer["Pan_no"].append(panno)
        mobno = int(input("Enter your mobile number--->"))
        coustmer["Mob_no"].append(mobno)
        password = getpass("Please enter your password--->")
        coustmer["Password"].append(password)
        coustmer["Amount"].append(0)

        with open("first.json","r+") as up:
            up.seek(0)
            js.dump(coustmer,up)
            up.truncate()
        with open("first.json") as up:
            data = js.load(up)
            u=data['Name']
            if username in u:
                uid=data['Name'].index(username)
        coustmer['Account_no'].append(a[uid])
        with open("first.json","r+") as f:
                actno=a[uid]
                js.dump(coustmer,f)

        print(f"this is your account no {actno}")
    elif copt ==2:
        print("Open Saving Account")
        username = input("Please enter your name--->")
        coustmer["Name"].append(username)
        dob = input("Enter your date of birth")
        coustmer["DOB"].append(dob)
        addharno = int(input("Please enter your 16 digit addhar card number--->"))
        coustmer["Addhar_no"].append(addharno)
        panno = input("Enter your pan card number-->")
        coustmer["Pan_no"].append(panno)
        mobno = int(input("Enter your mobile number-->"))
        coustmer["Mob_no"].append(mobno)
        password = getpass("Please enter your password--->")
        coustmer["Password"].append(password)
        amt = int(input("Deposit minimum 1000 Rs. to open a account--->"))

        while amt<1000:
            amt = int(input("Deposit minimum 1000 Rs. to open a account--->"))
        coustmer["Amount"].append(amt)
        with open("first.json","w") as up:
            up.seek(0)
            js.dump(coustmer,up)
            up.truncate()
        with open("first.json") as up:
            data = js.load(up)
            u=data['Name']
            if username in u:
                uid=data['Name'].index(username)
        coustmer['Account_no'].append(a[uid])
        with open("first.json","r+") as f:
                actno=a[uid]
                js.dump(coustmer,f)

        print(f"this is your account no {actno}")
    else:
        print("Invalid Input")
