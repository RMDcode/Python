def Add(no1,no2):
    Ans=no1+no2
    print("Addition of two number is :",Ans)

def main():
    print("Enter first number :",end="")
    val1=int(input())
    print("Enter second number :",end="")
    val2=int(input())
    Add(val1,val2)

if __name__=="__main__":
    main()
