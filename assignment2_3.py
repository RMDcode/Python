def factorial(No):
    
    if(No<0):
        print("Please enter the positive number!!!!")
        
    else:
        i=0
        fact=1
        for i in range(1,No+1):
            
            fact=fact*i
        return fact
    
def main():
    i=0
    print("Enter the number: ",end="")
    i=int(input())
    print(factorial(i))

if __name__=="__main__":
    main()