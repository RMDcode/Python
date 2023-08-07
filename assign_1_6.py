def ChkNum(i):
    if(i>0):
        print("Positive Number")
    if(i<0):
        print("Negative Number")
    if(i==0):
        print("Zero")

def main():
    print("enter any number :",end="")
    no=int(input())
    ChkNum(no)

if __name__=="__main__":
    main()