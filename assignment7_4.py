import os
import threading

def small(value):
    count=0
    for i in value:
        if('a'<=i<='z'):
            count=count+1
    print("Number of small characters :",count)

def capital(value):
    count=0
    for i in value:
        if('A'<=i<='Z'):
            count=count+1
    print("Number of Capital characters :",count)

def digits(value):
    count=0
    for i in value:
        if('0'<=i<='9'):
            count=count+1
    print("Number of small characters :",count)

def main():
    str=input("Enter the string :")

    t1=threading.Thread(target=small,args=(str,))
    t2=threading.Thread(target=capital,args=(str,))
    t3=threading.Thread(target=digits,args=(str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__=="__main__":
    main()