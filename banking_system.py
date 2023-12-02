# Parent Class 
class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("Personal Details----->")
        print("Name ",self.name)
        print("Age ",self.age)
        print("Gender ",self.gender)
        print("")

# Child class  
class Bank (User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance=0

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Amount balance has been updated : $",self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("Insufficient Funds | Balance Available : $",self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Account balance has been updated : $",self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance has been accepted : $",self.balance)

# Main function calling 
showDetails=User('Jyoti',21,'Female')
showDetails.show_details()

user1=Bank('Jyoti',22,'Female')
user1.deposit(200)
user1.withdraw(5)
user1.view_balance()
