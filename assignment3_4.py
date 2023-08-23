def main():
    print("Number of Elements :",end="")
    Length=int(input())

    Arr=list()

    print("Input elements :")
    for i in range(Length):
        value=int(input())
        Arr.append(value)

    Search=int(input("Enter the number to find its frequency :"))
    freq=0
    
    for num in Arr:
        if(num==Search):
            freq=freq+1

    print("output :",freq)

if __name__=="__main__":
    main()