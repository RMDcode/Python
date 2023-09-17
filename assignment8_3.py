import sys

def Display(no1):
    if(no1>0):
        print(no1,end="")
        Display(no1-1)
    
def main():
    print("Enter the number :",end="")
    no=int(input())

    k=Display(no)



if __name__=="__main__":
    main()