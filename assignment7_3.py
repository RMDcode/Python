import os
import threading

def even_list(arr):
    sum=0
    for num in arr:
        if(num%2==0):
            sum=sum+num
    print("Sum of even elements:",sum)

def odd_list(arr):
    sum = 0
    for num in arr:
        if(num%2!=0):
            sum=sum+num
    print("Sum of odd elements:",sum)

def main():
    print("Enter number of elements that you want to store:")
    length=int(input())

    arr=list()

    print("Enter the elements:")

    for i in range(length):
        value=int(input())
        arr.append(value)

    print("Elements from the list are:")
    for j in arr:
        print(j)

    t1 = threading.Thread(target=even_list, args=(arr,))
    t2 = threading.Thread(target=odd_list, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
