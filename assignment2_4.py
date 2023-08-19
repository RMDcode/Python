def factors(no):
    sum=0
    i=0
    for i in range(1,no+1):
        if(no%i==0):
            sum=sum+i
    return sum
            

def main():
    ret=0
    print("Enter the number :",end="")
    ret=int(input())
    print("output :",factors(ret))


if __name__=="__main__":
    main()