import json as js
def deposit():
    print("Cash Deposit")
    actnum = input("Enter your account number->")
    with open("first.json","r+") as up:
        data = js.load(up)
        an=data["Account_no"]
    if actnum in an:
        userid = data["Account_no"].index(actnum)
        username=data['Name'][userid]

        print(f"Hello! {username}")
        depoamt = int(input("Enter ammount for deposit"))

       #depname = input("Please enter depositor's name-->")
        amt=data['Amount'][userid]
        print(amt)
        c = amt+depoamt
        print("Total",c)
        coustmer["Amount"][userid] = c
        with open("first.json","r+") as f:
                js.dump(coustmer,f)
        print(f"Total available Balance-->{c}")
    else:
        print("Data not Stored")
