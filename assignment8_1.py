import sys

def Display(no1):
    if(no1>0):
        print("*",end="")
        Display(no1-1)
    
def main():
    print("Enter the number :",end="")
    no1=int(input())

    k=Display(no1)



if __name__=="__main__":
    main()