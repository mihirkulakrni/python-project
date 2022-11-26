#bank project

print("welcome to bank")
name = (input("Enter your name here:"))
print  ("welcome",name,"to ,BANK OF MIHIR")
print ("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(input("enter your account number"))
class bank:
    def __init__(self):
        self.balance = 0
        print("your account is crated")

    def deposit(self):
        amount = int(input("enter the amount to deposit in your account:"))
        self.balance = self.balance + amount
        print("deposit is suceesful and the balance in account is %f" % self.balance)

    def withdarw(self):
         amount = float(input("enter the amount to withdarw:"))
         if (self.balance >= amount):
             self.balance = self.balance - amount
             print("withdraw suceesfull and balance is %f" % self.balance)
         else:
             print ("insufficient balance")
    def enquiry(self):
        print("balance in your accountis%f" % self.balance)          
acc = bank()
acc.deposit()
acc.withdarw()
acc.enquiry()
