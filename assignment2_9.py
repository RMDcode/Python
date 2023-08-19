def count(no):
    count=0

    while(no>0):
        no = no // 10

        count=count+1
    
    return count

def main():
    i=0
    print("Enter the number :",end="")
    i=int(input())
    print(count(i))


if __name__=="__main__":
    main()