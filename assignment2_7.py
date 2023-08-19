def pattern(no):
    i=0
    for i in range(1,no+1):
        j=0
        for j in range(1,no+1):
            print(j,end="")
        print()


def main():
    i=0
    print("Enter the number :",end="")
    i=int(input())
    pattern(i)

if __name__=="__main__":
    main()