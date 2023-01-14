class User:
    def __init__(self, name, pin, password):
        self.name=name
        self.pin=pin
        self.password=password

    def change_name(self, name):
        self.name=name
        # print("You have changed your name to", name)

    def change_pin(self, pin):
        self.pin=pin
        # print("You have changed your pin to", pin)

    def change_password(self, password):
        self.password=password
        # print("You have changed your password to", password)

#Task 4 it won't print out what I want it to
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance=0

    def show_balance(self):
        print(self.name, "has a balance of:", self.balance)

    def withdraw(self, withdraw):
        self.balance-=withdraw

    def deposit(self, deposit):
        self.balance+=deposit
#task 5
    def transfer_money(self, transfer):
        #transfer=input("How much are you transferring?") #this is wrong
        print("You are transferring", transfer ,"to", self.name)
        print("Authentification required")
        required=input("Enter your pin: ")
        if required==self.pin:
            print("Transfer authorized\nTransferring $"+str(transfer), "to", self.name)
            
            #how do I do the math here?
            return True
        else:
            False
    
#testing code
""" Driver Code for Task 4"""
bank1=BankUser("Bob", "1234", "password")
print("you are here")
bank1.show_balance()
bank1.deposit(1000)
print("you are here")
bank1.show_balance
print("you are here")
bank1.withdraw(500)
bank1.show_balance

""" Driver Code for Task 5"""
bank2=BankUser("Mars", "4321", "pass")
bank2.deposit(5000)
bank2.show_balance
bank1.show_balance
bank2.transfer_money(500)
bank2.show_balance
bank1.show_balance

# """ Driver Code for Task 1 """
# user1=User("Bob", 1234, "Password")
# print(user1.name, user1.pin, user1.password)
# """ Driver Code for Task 2 """
# user1.change_name("Bobby")
# user1.change_pin("4321")
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)
# """ Driver Code for Task 3"""
# bank1=BankUser("Bob", 1234, "password", balance)
# print(bank1.name, bank1.pin, bank1.password, bank1.balance)
