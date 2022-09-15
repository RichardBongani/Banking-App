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
        self.initial_depo = initial_depo
        self.pin = pin
        