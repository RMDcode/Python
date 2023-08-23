def main():
    print("Number of Elements :",end="")
    Length=int(input())

    Arr=list()

    print("Input elements :")
    for i in range(Length):
        value=int(input())
        Arr.append(value)

    sum=0
    print("Output :")
    for i in range(len(Arr)):
        sum=sum+Arr[i]

    print(sum)


if __name__=="__main__":
    main()