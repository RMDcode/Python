def main():
    print("Number of elements :",end="")
    Length=int(input())

    Arr=list()

    print("Input Elements :")
    for i in range(Length):
        value=int(input())
        Arr.append(value)

    max_element = Arr[0]
    for i in range(1, len(Arr)):
        if(Arr[i] > max_element):
            max_element = Arr[i]

    print("Output:", max_element)

if __name__=="__main__":
    main()