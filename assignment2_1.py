import Arithmetic

def operations():
    print("Please enter First number :",end="")
    n1=int(input())
    print("Please enter Second number :",end="")
    n2=int(input())
    Arithmetic.Addition(n1,n2)
    Arithmetic.Substraction(n1,n2)
    Arithmetic.Multiplication(n1,n2)
    Arithmetic.Division(n1,n2)
    


def main():
    operations()


if __name__=="__main__":
    main()