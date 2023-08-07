def star(val):
    i=0
    data=range(val)
    for i in range(6):
        print("*",end="")

def main():
    print("put any number :")
    no=int(input())
    star(no)

if __name__=="__main__":
    main()



