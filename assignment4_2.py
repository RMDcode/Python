multiplication = lambda no1,no2:(no1*no2)

def main():
    i=0
    a=0
    b=0
    print("Enter the first number :",end="")
    a=int(input())
    print("Enter the second number :",end="")
    b=int(input())

    print("output",multiplication(a,b))

if __name__=="__main__":
    main()