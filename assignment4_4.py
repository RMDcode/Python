import functools

Even=lambda no: no%2==0
increase=lambda no:no*(no)
product=lambda a,b:a+b

def main():
    a=[]
    print("Enter the elements :",end="")
    size=int(input())

    print("Enter the numbers :")
    for i in range(size):
        i=int(input())
        a.append(i)

    output=list(filter(Even,a))
    print("Filter :",output)
    output1=list(map(increase,output))
    print("Map :",output1)
    output2=functools.reduce(product,output1)
    print("Reduce :",output2)


if __name__=="__main__":
    main()