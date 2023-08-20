def pattern(no):
    i=0
    j=0
    for i in range(1,no+i+1):
        for j in range(1,i+1):
            print(j,end="")
        print()


def main():
    i=0
    print("Enter the number :",end="")
    i=int(input())
    pattern(i)

    

if __name__=="__main__":
    main()