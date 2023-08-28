class Demo:
    value=0                                 #class variable

    def __init__(self,number1,number2):
        self.no1=number1                    #instance variable
        self.no2=number2                    #instance variable

    def fun(self):                          #instance method
        print("From Fun Values of Number1:",self.no1)
        print("From fun Values of Number2:",self.no2)

    def gun(self):                          #instance method
        print("From gun Values of Number1:",self.no1)
        print("From gun Values of Number2:",self.no2)




def main():
    i1=0
    i2=0
    i3=0
    i4=0
    print("Enter number :",end="")
    i1=int(input())
    print("Enter number :",end="")
    i2=int(input())
    print("Enter number :",end="")
    i3=int(input())
    print("Enter number :",end="")
    i4=int(input())

    obj1=Demo(i1,i2)
    obj2=Demo(i3,i4)

    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()

if __name__=="__main__":
    main()