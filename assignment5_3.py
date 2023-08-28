class Arithmetic:
    
    def __init__(self, value1=0, value2=0):
        self.val1 = value1
        self.val2 = value2
        self.Add= 0
        self.Sub= 0
        self.Mult= 0
        self.Div= 0
    
    def Accept(self):
        print("Enter the value1:", end="")
        self.val1=int(input())
        print("Enter the value2:", end="")
        self.val2=int(input())
    
    def Addition(self):
        self.Add=self.val1+self.val2
            
    def Substraction(self):
        self.Sub=self.val1-self.val2        
    
    def Multiplication(self):
        self.Mult=self.val1*self.val2        
    
    def Division(self):
        self.Div=self.val1/self.val2        
    

    def Display(self):
        print("Addition:", self.Add)
        print("Substraction:", self.Sub)
        print("Multiplication:", self.Mult)
        print("Division:", self.Div)

def main():
    obj = Arithmetic()
    obj.Accept()
    obj.Addition()
    obj.Substraction()
    obj.Multiplication()
    obj.Division()
    obj.Display()

if __name__ == "__main__":
    main()
