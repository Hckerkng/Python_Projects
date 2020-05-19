from getpass import getpass
import json as js
import os
def main():
    print("Welcome to Our bank we are happy to help you..")
    opt = int(input("Select any Option --> \n1.Banking\n2.Loan\n3.Master Login\n4.Exit"))
    def banking():
        print("Thanks for choosing banking with us")
        bopt = int(input("Select any Option--> \n1.Cash Withdrawl\n2.Cash Deposit\n3.Balance Enquiry\n4.Open an Account\n5.Update Details\n6.Back"))
# Cash Withdrawl
        if bopt == 1:
            print("Please enter your username and password")
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
                wamount = int(input("Please Enter amount"))
                amt=data['Amount'][userid]
                rb = amt - wamount
                coustmer["Amount"][userid] = rb
                with open("first.json","r+") as f:
                        js.dump(coustmer,f)
                print(f"Available Balance-->{rb}")
            else:
                print("Invalid username and password")
#Cash Deposit
        elif bopt == 2:
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
#Balance Enquiry
        elif bopt == 3:
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
#Create Account
        elif bopt == 4:
            print("Create an Account")
            copt = int(input("Select any option-->\n1.Current Account\n2.Saving Account\n"))
            def printWellOrdered(number, x, k):
                if (k == 0):
                    d ='1000'+str(number)
                    a.append(d)
                for i in range( (x + 1), 10):
                    printWellOrdered(number * 10 + i, i, k - 1)
            def generateWellOrdered(k):
                printWellOrdered(0, 0, k)
            if __name__ == "__main__":
                k = 4
            generateWellOrdered(k)
            if copt == 1:
                print("Open Current Account")
                username = input("Please enter your name\n")
                coustmer["Name"].append(username)
                dob = input("Enter your date of birth\n")
                coustmer["DOB"].append(dob)
                addharno = int(input("Please enter your 16 digit addhar card number\n"))
                coustmer["Addhar_no"].append(addharno)
                panno = input("Enter your pan card number\n")
                coustmer["Pan_no"].append(panno)
                mobno = int(input("Enter your mobile number\n"))
                coustmer["Mob_no"].append(mobno)
                password = getpass("Please enter your password\n")
                coustmer["Password"].append(password)
                coustmer["Amount"].append(0)

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
            elif copt ==2:
                print("Open Saving Account")
                username = input("Please enter your name")
                coustmer["Name"].append(username)
                dob = input("Enter your date of birth")
                coustmer["DOB"].append(dob)
                addharno = int(input("Please enter your 16 digit addhar card number-->"))
                coustmer["Addhar_no"].append(addharno)
                panno = input("Enter your pan card number-->")
                coustmer["Pan_no"].append(panno)
                mobno = int(input("Enter your mobile number-->"))
                coustmer["Mob_no"].append(mobno)
                password = getpass("Please enter your password")
                coustmer["Password"].append(password)
                amt = int(input("Deposit minimum 1000 Rs. to open a account"))

                while amt<1000:
                    amt = int(input("Deposit minimum 1000 Rs. to open a account"))
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

#Update Details
        elif bopt == 5:
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

#Back
        elif bopt == 6:
            main()
        else:
            print("Invalid Input")

#Loan Procedure
    def Loan():
        print("For Loan You Should have an account in bank")
        actnum = int(input("Enter your account number"))
        lopt = int(input("Select any option--> \nEmployeement status\n1.Govt. Job\n2.Pvt. Job\n3.Bussiness\n4.Student\n5.Back"))
#Gov. Job
        if lopt == 1:
            print("Government Employee")
            inc = int(input("Please enter your monthly income"))
            if inc >= 50000:
                print("You are eligible for loan of 2 lac only")
                salslip = input("attach salary sleep")
                bankstat = input("attach bank Statement of 6 months")
            elif inc >= 100000:
                print("You are eligible for loan of 5 lac only")
                salslip = input("attach salary sleep")
                bankstat = input("attach bank Statement of 6 months")
            elif inc >= 200000:
                print("You are eligible for loan of 10 lac only")
                salslip = input("attach salary sleep")
                bankstat = input("attach bank Statement of 6 months")


#Pvt Job
        elif lopt == 2:
            print("Private Job")
            inc = int(input("Please enter your monthly income"))
            if inc >= 50000:
                print("You are eligible for loan of 1 lac only")
                cname = input("Please enter your monthly income")
                desig = input("Enter Designation")
                salslip = input("Attach salary sleep")
                bankstat = input("Attach bank Statement of 6 months")
                itr = input("Attach ITR of 3 years")
            elif inc >= 100000:
                print("You are eligible for loan of 2.5 lac only")
                cname = input("Please enter your monthly income")
                desig = input("Enter Designation")
                salslip = input("Attach salary sleep")
                bankstat = input("Attach bank Statement of 6 months")
                itr = input("Attach ITR of 3 years")
            elif inc >= 200000:
                print("You are eligible for loan of 4 lac only")
                cname = input("Please enter your monthly income")
                desig = input("Enter Designation")
                salslip = input("Attach salary sleep")
                bankstat = input("Attach bank Statement of 6 months")
                itr = input("Attach ITR of 3 years")


    #Bussiness
        elif lopt == 3:
            print("Bussiness")
            inc = int(input("Please enter your monthly income"))
            if inc >= 50000:
                print("You are eligible for loan of 75000K only")
                nofb = input("Please enter Business Name")
                loc = input("Enter Location of Business")
                bank_stat = input("Attach bank Statement of 6 months")
                itr = input("Attach ITR of 3 years")
                run_loans = print("running loans")
            elif inc >= 100000:
                print("You are eligible for loan of 2 lac only")
                cname = input("Please enter your monthly income")
                desig = input("Enter Designation")
                sal_slip = input("Attach salary sleep")
                bank_stat = input("Attach bank Statement of 6 months")
                itr = input("Attach ITR of 3 years")
                run_loans = print("Run loans")
            elif inc >= 200000:
                print("You are eligible for loan of 3.5 lac only")
                cname = input("Please enter your monthly income")
                desig = input("Enter Designation")
                sal_slip = input("Attach salary sleep")
                bank_stat = input("Attach bank Statement of 6 months")
                itr = input("Attach ITR of 3 years")
                run_loans = print("Run loans")
            else:
                print("You are not Eligible")
#Student
        elif lopt == 4:
            print("Student")
            print("Sorry we can't help you")
        elif lopt == 5:
            main()
        else:
            print("Invalid Input")
#3 Master Login
    def Master_Login():
        mang_id = input("Enter your username")
        mang_pswd = input("Enter your Password")
        print("Status")
    def exit():
        print("Thanks for choosing banking with us")
    if opt == 1:
        banking()
    elif opt == 2:
        Loan()
    elif opt == 3:
        Master_Login()
    elif opt == 4:
        pass
    else:
        print("Wrong Input")
