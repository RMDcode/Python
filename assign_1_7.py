def accept(i):
    if(i%5==0):
        print("True")
    else:
        print("False")
        
def main():
    print("Enter number :")
    num=int(input())
    accept(num)

if __name__=="__main__":
    main()