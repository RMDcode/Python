import os
import threading

def even(value):
    i=1
    print("First 10 odd numbers")
    for i in range(value):
        if(i%2==0):
            print(i)
    

def odd(value):
    i=1
    print("First 10 odd numbers")
    for i in range(value):
        if(i%2!=0):
            print(i)


def main():
    No=20
    t1=threading.Thread(target=even,args=(No,))
    t2=threading.Thread(target=odd,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()