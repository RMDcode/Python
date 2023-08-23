def prime(no):
    if(no<=1): 
        return False

    if(no<=3):
        return True

    if( no%2==0 or no%3==0):
        return False


    i=5
    while(i*i<=no):
        if(no%i==0 or no%(i+2)==0):
            return False
        i=i+6
    return True


def main():
    print("Number of elements :",end="")
    Length=int(input())

    Arr=list()

    print("Input Elements :")
    for i in range(Length):
        value=int(input())
        Arr.append(value)

    sum = 0
    for j in Arr:
        if prime(j):
            sum = sum+ j
            

    print("Output :", sum)


if __name__=="__main__":
    main()