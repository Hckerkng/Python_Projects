from withdrawl import withdrawl
from deposit import deposit
from update_details import update_details
from create_account import create_account
from bal_enquiry import bal_enquiry
def banking():
    print("Thanks for choosing banking with us")
    bopt = int(input("Select any Option--> \n1.Cash Withdrawl\n2.Cash Deposit\n3.Balance Enquiry\n4.Open an Account\n5.Update Details\n6.Back"))
    if bopt ==1:
        withdrawl()
    if bopt ==2:
        deposit()
    if bopt ==3:
        bal_enquiry()
    if bopt ==4:
        create_account()
    if bopt ==5:
        update_details()
    if bopt ==6:
        banking()
    else:
        print("Invalid Input")