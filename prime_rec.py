"""this module has a function prime to check wheather a number is prime or not.
using recursion
"""
from math import sqrt, ceil
import platform
import os
import time

def clr_scr():
    """clr_scr() --> used to clear terminal screen
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system("clear")

def prime(num, check=2):
    """prime(num, check=2) return True if num is prime else return False
    """
    if check == ceil(sqrt(num))+1:
        return True
    if num % check == 0:
        return False
    return prime(num, check+1) #recursion

if __name__ == "__main__":
    clr_scr()
    print("\n\n\tWelcome to Prime Program\n\n")
    while input("\n\n\n\t\tPress any to run prime checker "):
        clr_scr()
        num = int(input("\n\n\t\tEnter a number : "))
        print("\n\n\n\t\t\t", end="")
        for var in range(10):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("Processing", end="")
        for var in range(10):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n\n")
        if prime(num):
            print(f"\n\n\t\t\t{num} is a Prime Number.")
        else:
            print(f"\n\n\t\t\t{num} is not a Prime Number.")
            break
    else:
        print("\n\n\t\tBye Bye user")
        time.sleep(3)
        clr_scr()
