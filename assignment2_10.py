def main():
    print("Enter number of digits that you want :",end="")
    length=int(input())

    Arr=list()

    print("Enter the number :",end="")

    for i in range(length):
        value=int(input())
        Arr.append(value)

    sum=0
    cnt=0

    for cnt in range(0,len(Arr)):
        sum=sum+Arr[cnt]

    return print("Output:",sum)
    
    

if __name__=="__main__":
    main()