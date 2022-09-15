import random as r

#User Class Here: 
class User():
    #Constructor
    print("Welcome to King Bank (PTY)Ltd\n")
    def __init__(self,name,age,gender,tel_num,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel_num = tel_num
        self.address = address
        
    #Bank Registration Here:
    def account_holder(self):
        print('PLEASE BEGIN REGISTRATION:\n')
        self.name = input('Enter your name:\n ')
        self.age = input('Enter your age:\n ')
        self.gender = input('Enter your Gender:\n ')
        self.tel_num = input('Enter your Contact Number:\n ')
        self.address = input('Enter your Home Addess:\n ')
        print(f'\nHello there, {self.name}, Welcome to King Bank. Your balance is R0.00 please make a deposit ')
        
    #Checking if person is employee
    def user_details(self):
        print(f"Thank you, {self.name} with tel {self.tel_num} for choosing us")
        
#Bank Account Class Here:      
class BankAccount(User):
    acc_numb = 0
    
    def __init__(self,name,age,gender,tel_num,address,initial_deposit,pin):
        super().__init__(name,age,gender,tel_num,address)
        self.acc_balance = initial_deposit
        self.acc_num = BankAccount.acc_numb
        self.pin = pin
        
        BankAccount.acc_numb = BankAccount.acc_numb + r.randrange(999999999999)
    
    def show_details(self):
        print(f'Hi {self.name}\t with Account Number: {self.acc_numb}\t Your Current Balance is R{self.acc_balance}')
        
    def deposit(self):
        dep_amount = int(input("Enter Deposit Amount"))
        if dep_amount > 0:
            self.acc_balance = self.acc_balance + dep_amount
            print(f"Successfully Deposited, Current Balance: R{self.acc_balance}")
        else:
            print("Invalid Amount, Try Again")
            
#Creating an Object
if __name__ == '__main__':
    
    customer1 = BankAccount(name ='',age= '',gender = '',tel_num='0681783394',address='110 Pine Ave Centurion', initial_deposit= 1500, pin= 1988)
    customer1.account_holder()
    print(customer1.show_details())
    customer1.deposit()
    