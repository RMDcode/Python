import os
import threading

def even_factor(value):
    sum=0
    for i in range(1,value+1):
        if(value%i==0 and i%2==0):
            sum=sum+i
    print("Sum of even factors :",sum)

def odd_factor(value):
    sum=0
    for i in range(1,value+1):
        if(value%i==0 and i%2!=0):
            sum=sum+i
    print("Sum of odd factors :",sum)

def main():
    No=int(input("Enter the inetger:"))

    t1=threading.Thread(target=even_factor,args=(No,))
    t2=threading.Thread(target=odd_factor,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()