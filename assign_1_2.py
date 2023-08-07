def ChkNum(data):
    if(data%2==0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Please enter number :",end="\n")
    i=int(input())
    ChkNum(i)

if __name__=="__main__":
    main()