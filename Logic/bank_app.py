from os import access
import random as r

#User Class Here: 
class User():
    #Constructor
    print("WELCOME TO KING BANK (PTY)Ltd\n")
    def __init__(self,name,age,gender,tel_num,address,city):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel_num = tel_num
        self.address = address
        self.city = city
        
    #Bank Registration Here:
    def account_holder(self):
        print('PLEASE BEGIN REGISTRATION:\n')
        self.name = input('Enter your name:\n ')
        self.age = input('Enter your age:\n ')
        self.gender = input('Enter your Gender:\n ')
        self.tel_num = input('Enter your Contact Number:\n ')
        self.address = input('Enter your Home Addess:\n ')
        self.city = input('Enter your City:\n')
        self.account_type= input('Enter Account Type(Savings/Cheque)\n')
        print("WELCOME NEW USER\n")
        print(f'\nHello there, {self.name}, Welcome to King Bank. Your balance is R0.00 please make a deposit ')
        
    #Checking if person is employee
    def user_details(self):
        print(f"Thank you, {self.name} with tel {self.tel_num} for choosing us")
        
#Bank Account Class Here:      
class BankAccount(User):
    acc_numb = 0
    
    def __init__(self,name,age,gender,tel_num,address,city,account_type,branch_code,initial_deposit,pin):
        super().__init__(name,age,gender,tel_num,address,city)
        self.acc_balance = initial_deposit
        self.account_type = account_type
        self.branch_code = branch_code
        self.acc_num = BankAccount.acc_numb
        self.pin = pin
        BankAccount.acc_numb = BankAccount.acc_numb + r.randrange(999999999999)
    
    def show_details(self):
        print('YOUR BANK DETAILS: \n')
        print(f'Account Number Is: {self.acc_numb}\nBranch:{self.city}\nAccount Type:{self.account_type}\nCurrent Balance is R{self.acc_balance}\nBranch Code:{self.branch_code}')        

    #Displaying Account Balance
    def balance(self):
        print(f'Your Account Balance is R{self.acc_balance}')
        
#Method for doing bank deposits:       
    def deposit(self):
        dep_amount = int(input('Enter Deposit Amount: '))
        if dep_amount > 0:
            self.acc_balance = self.acc_balance + dep_amount
            print(f'Successfully Deposited, Current Balance: R{self.acc_balance}')
        else:
            print('Invalid Amount, Try Again')

#Method for withdrawing money:
    def withdraw(self):
        min_withdrawal = 10
        with_amount = int(input('Enter Withdrawal Amount: '))
        if with_amount <= self.acc_balance and with_amount > 10:
            self.acc_balance = self.acc_balance - with_amount
            print(f'Successfull Withdrawal, Current Balance: {self.acc_balance}')
        else:
            print('Invalid Amount, Try again') 

#Method is for making a payment:
    def payment(self,other):
        min_payment = 50
        # pay = input('Press 1 to pay cust1 or 2 to pay cust2')
        payment_amount = int(input('Enter Payment Amount: '))
        if payment_amount > min_payment and payment_amount <= self.acc_balance:
            self.acc_balance = self.acc_balance - payment_amount
            other.acc_balance = other.acc_balance + payment_amount
            print(f'Payment Sent: -R{payment_amount}\t Current Balance: R{self.acc_balance}\n')
            #Displays money that was sent
            print('MONEY IN & BALANCES: ')
            print(f'You have received: +R{payment_amount}\nNew Balance: R{other.acc_balance}')
        else:
            print('Invalid Amount, Try again')
            
#Who are you paying:
    
        
#Creating an Object
if __name__ == '__main__':
    
    customer1 = BankAccount(name ='',age= '',gender = '',tel_num='',address='',city='',account_type='',branch_code=225005, initial_deposit= 5000, pin= 1988)
    customer2 = BankAccount(name ='',age= '',gender = '',tel_num='',address='',city='',account_type='',branch_code=225005, initial_deposit= 2000, pin= 1988)
    
    while True:
        
        choose_input = int(input('How can we help you?\n\nPick 1 to view balance\nPress 2 to deposit\nPress 3 to Withdraw\nPress 4 to make Payment: '))
        
        if choose_input == 1:
            customer1.balance()
        elif choose_input == 2:
            customer1.deposit()
        elif choose_input == 3:
            customer1.withdraw()
        elif choose_input == 4:
            customer1.payment(customer2)
        else:
            print('Invalid, try again')
        break
    # customer1.account_holder()
    # print(customer1.show_details())
    # customer1.deposit()
    # customer1.withdraw()
    # customer1.payment()
    # customer1.payment(customer2)
    # customer2.payment(customer1)
    
    