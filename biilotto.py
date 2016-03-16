#!/usr/bin/python3
from pymongo import MongoClient
import random
import sys

#variable
nMin = 0
nMax = 99
title = r'''
\\\\================================////
||||                                ||||
        Welcome to BiiLotto
        Author: Bii811              
||||                                ||||
////================================\\\\
'''

def isWin(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2) 
        return True if num1 == num2 else False
    except ValueError:
        print("[-] Input Error!")

def isNumberInRange(value, nMin, nMax):
    try:
        value = int(value)
        nMin = int(nMin)
        nMax = int(nMax)
        if nMin <= nMax:
            if nMin <= value <= nMax:
                return True
            else:
                print("[-] Only number in %d-%d is allowed!" % (nMin, nMax))
                return False
        else:
            print("[-] min number must less than or equal max number!")
    except ValueError:
        print("[-] Only number is allowed!")

def Lotto(iNum, nMin, nMax):
    if isNumberInRange(iNum, nMin, nMax):
        iNum = int(iNum)
        nMin = int(nMin)
        nMax = int(nMax)
        lottoNum = random.randint(nMin, nMax)
        print("Lotto number is %d." % lottoNum)
        print("Your number is %d." % iNum)
        if isWin(iNum, lottoNum):
            print("*** Congratulation! You Win! ***")
        else:
            print("Sorry, you lose! Please try again!")
    
def main(argv):
    if len(argv) == 3:
        iNum = argv[0]
        numMin = argv[1]
        numMax = argv[2]
        Lotto(iNum, numMin, numMax)
    else:
        print(title)
        while(True):
            numMin = nMin
            numMax = nMax
            iNum = input("What is your lucky number (%d-%d): " % (numMin, numMax))
            Lotto(iNum, numMin, numMax)
            print()

if __name__ == "__main__":
        main(sys.argv[1:])
