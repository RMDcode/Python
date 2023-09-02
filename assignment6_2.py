class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.HolderName=Name
        self.Balance=Amount
        self.interest=0  

    def Deposit(self,Amount):
        self.Balance = self.Balance + Amount

    def withdrawl(self,Amount):
        if self.Balance<Amount:
            print("There is no sufficient balance")
            print("<----------------------------------------------------------->")
        else:
            self.Balance=self.Balance-Amount
            print("Amount withdrawal successfully.....")
            print("<----------------------------------------------------------->")

    def CalculateInterest(self):
        self.interest=(self.Balance*BankAccount.ROI)/100

    def Display(self):
        print("Account Holder Name:",self.HolderName)
        print("Your Current Balance:",self.Balance)
        print("Your Interest:",self.interest)

def main():
    print("Enter name:",end="")
    name = input()
    print("Enter initial balance:", end="")
    amount = float(input()) 
    obj = BankAccount(name, amount)
    print("Enter deposit amount:", end="")
    deposit_amount = float(input())
    obj.Deposit(deposit_amount)
    print("Enter withdrawal amount:", end="")
    withdrawal_amount = float(input())
    obj.withdrawl(withdrawal_amount)
    obj.CalculateInterest()
    obj.Display()
   
if __name__ == "__main__":
    main()
