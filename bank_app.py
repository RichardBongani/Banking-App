import random
class User():
    #Constructor
    def __init__(self,name,age,gender,tel_num,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel_num = tel_num
        self.address = address
        
    #Checking if person is employee
    def user_details(self):
        print(f"Thank you, {self.name} with tel {self.tel_num} for choosing us")
        
class BankAccount(User):
    acc_numb = 2799758187
    
    def __int__(self,name,age,gender,tel_num,address,initial_depo,pin):
        super().__init__(name,age,gender,tel_num,address)
        self.acc_balance = initial_depo
        self.acc_num = BankAccount.acc_numb
        self.pin = pin
        
        
        BankAccount.acc_numb = BankAccount.acc_numb + 1
    
    def show_details(self):
        print(f"Hi, {self.name}, with Account Number: {self.acc_numb} Your Current Balance is {self.acc_balance}")
        
    def deposit(self):
        dep_amount = int(input("Enter Deposit Amount"))
        if dep_amount > 0:
            self.acc_balance = self.acc_balance + dep_amount
            print(f"Successfully Deposited, Current Balance: R{self.acc_balance}")
        else:
            print("Invalid Amount, Try Again")
            