"""This is the Simple Libraray Management Project module
Usages: python Library management.py
"""
from copy import deepcopy
from pprint import pprint
books = {"cs":["Web Tech","c","c++","python","java"],
         "stat":["inference","Multivar","DOE","Prob"],
         "elec":["Phy","Maths","thermo","C"],
         "civil":["Autocad","Maths","servay"]
        }
deplist = list(books)
student_list = {}

avalbooks = deepcopy(books)
while True:
    print("*"*20)
    print("Library Management")
    print("*"*20)
    option = int(input("Select any Options -> \n1.Student Registration\n2.Book Issue\n3.Add Books\n4.Status Of Books\n5.Students Status\n6.Exit"))
    if option == 1:
        name = input("Enter your name")
        age = int(input("Enter your age"))
        student_list.setdefault(name,[])
        student_list.setdefault(age,[])
        sid_list = list(student_list)
        print("Your Student id is = ",sid_list.index(name))
    elif option == 2:
        dep = int(input(f"Select your Dep.--> \n0.{deplist[0]}\n1.{deplist[1]}\n2.{deplist[2]}\n3.{deplist[3]}\n -->"))
        booklist = avalbooks.get(deplist[dep])
        book = int(input(f"Select any book {booklist}-->"))
        sid = int(input("Enter your Student id--> "))
        sname = sid_list[sid]
        student_list[sname].append(booklist[book])
        booklist.pop(book)
        books = dict(avalbooks)
    elif option == 3:
        dep_no = int(input(f"Select Dep.--> \n0.{deplist[0]}\n1.{deplist[1]}\n2.{deplist[2]}\n3.{deplist[3]}\n -->"))
        book_name = input("Enter name of book")
        dep_name = deplist[dep_no]
        books[dep_name].append(book_name)
    elif option == 4:
        pprint(avalbooks)
    elif option == 5:
        pprint(student_list)
    elif option == 6:
        break
    else:
        print("Wrong input")
    
