from banking import banking 
from loan import loan
from master_login import master_login

def main():
    print("Welcome to Our bank we are happy to help you..")
    opt = int(input("Select any Option --> \n1.Banking\n2.Loan\n3.Master Login\n4.Exit\n"))
    if opt == 1:
        banking()
    elif opt == 2:
        loan()
    elif opt == 3:
        master_login()
    elif opt == 4:
        exit()
    else:
        print("Wrong Input")
main()
