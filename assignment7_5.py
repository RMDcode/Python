import os
import threading

def Thread1(value):
    print("Thread1 print 1 to 50")
    for i in range(1,51):
        print(i)
    
def Thread2(value):
    print("Thread2 print 50 to 1")
    for i in range(50,0,-1):
        print(i)

def main():
    No=None
    t1=threading.Thread(target=Thread1,args=(No,))
    t2=threading.Thread(target=Thread2,args=(No,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
if __name__=="__main__":
    main()