import sys

def Display(no1):
    if(no1<10):
        return no1
    else:
        l=no1%10
        d=no1//10
        return l + Display(d)


def main():
    print("Enter the number :",end="")
    no=int(input())

    k=Display(no)
    print(k)

if __name__=="__main__":
    main()