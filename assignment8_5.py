import sys

def Display(no1):
    if(no1==0 or no1==1):
        return 1
    else:
        return no1 * Display(no1-1)


def main():
    print("Enter the number :",end="")
    no=int(input())

    k=Display(no)
    print("Summation",k)

if __name__=="__main__":
    main()