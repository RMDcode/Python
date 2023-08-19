def CheckPrime(no):
    i=0
    p=0

    if(no==0 or no==1):
        p=1
    
    for i in range(2,no//2+1):
        if(no%i==0):
            p=1
            break


    if(p==0):
        print("Number is prime")
    else:
        print("Number is not prime")



def main():
    i=0
    print("Enter the number:",end="")
    i=int(input())
    CheckPrime(i)

if __name__=="__main__":
    main()