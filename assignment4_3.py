import functools

equal=lambda no: 70<=no<=90
increase=lambda no:no+10
addition=lambda a,b:a*b

def main():
    a=[]
    print("Enter the elements :",end="")
    size=int(input())

    print("Enter the numbers :")
    for i in range(size):
        i=int(input())
        a.append(i)

    output=list(filter(equal,a))
    print("Filter :",output)
    output1=list(map(increase,output))
    print("Map :",output1)
    output2=functools.reduce(addition,output1)
    print("Reduce :",output2)


if __name__=="__main__":
    main()