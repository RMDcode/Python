class Number:
    def __init__(self, value):
        self.value = value

    def chkprime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True

    def chkperfect(self):
        sumfactors = sum(self.factors())
        return sumfactors == self.value

    def sumfactors(self):
        return sum(self.factors())

    def factors(self):
        factorslist = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                factorslist.append(i)
        return factorslist

def main():
    i = int(input("Enter a number: "))
    
    obj = Number(i)
    is_prime = obj.chkprime()
    is_perfect = obj.chkperfect()
    sum_factors = obj.sumfactors()
    factors_list = obj.factors()

    print("prime", is_prime)
    print("perfect number", is_perfect)
    print("Sum of factors of :", sum_factors)
    print("Factors of :", factors_list)

if __name__ == "__main__":
    main()