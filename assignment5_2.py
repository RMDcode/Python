class Circle:
    PI = 3.14  # Class variable
    
    def __init__(self, radius=0.0):
        self.radius=radius
        self.area=0.0
        self.circumference=0.0
    
    def Accept(self):
        print("Enter the radius:", end="")
        self.radius=float(input())
    
    def CalculateArea(self):
        self.area=self.PI*self.radius*self.radius
        #print("Area of circle is:", self.area)
    
    def CalculateCircumference(self):
        self.circumference=2*self.PI*self.radius
        #print("Circumference of Circle:", self.circumference)
    
    def Display(self):
        print("Radius:", self.radius)
        print("Area of Circle:", self.area)
        print("Circumference of Circle:", self.circumference)


def main():
    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()


if __name__ == "__main__":
    main()
