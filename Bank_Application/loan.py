def loan():
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