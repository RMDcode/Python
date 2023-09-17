import sys

def Display(no1,i=1):
    if(i<=no1):        
        print(i,end="")
        Display(no1,i+1)
    
def main():
    print("Enter the number :",end="")
    no=int(input())

    k=Display(no)



if __name__=="__main__":
    main()