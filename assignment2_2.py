def star(no1):
    i=0
    for i in range(no1):
        j=0
        for j in range(no1):
            print("*",end="")
        print()    

def main():
    print("Enter the number :",end="")
    no=int(input())

    k=star(no)



if __name__=="__main__":
    main()