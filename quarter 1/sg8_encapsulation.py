class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = int(account_number)
        self.__balance = float(balance)
        
    #public account number setter method
    def set_account_number(self, account_number):
        self.__account_number = account_number
    
    #public balance setter
    def set_balance(self, balance):
        if balance <0:
            print("The balance must not be a negative number.")
        else:
            self.__balance += balance

    #public account number getter method
    def get_account_number(self):
        return self.__account_number
    
    #public balance getter method
    def get_balance(self):
        return self.__balance

#displays account number and balance
def display_class(c):
    print("")
    print(f"""Account 1
Account Number : {c.get_account_number()}
Balance: {c.get_balance()}""")
    print("")

#program proper
a1 = BankAccount(12345,1000)  #sets bank account object
display_class(a1)             #displays initial info of bank account object
bal = float(input("Update balance to "))         #gets input of the user to update the balance
a1.set_balance(bal)                              #sets account object's balance
account_number = int(input("Account Number: "))  #gets input of the user to update the account number
a1.set_account_number(account_number)            #sets object's account number
display_class(a1)             #displays final info of bank account object after the program
