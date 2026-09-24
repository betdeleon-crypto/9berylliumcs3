import sys

class savingsAccount:
  def __init__(self, accountName, PIN, balance, kiddieAccs):
    self.accountName = str(accountName)
    self.PIN = int(PIN)
    self.balance = float(balance)
    self.kiddieAccs = []

  def code(self):
    code = int(input(f"Enter password for {self.accountName}: "))
    if code == self.PIN:
        return True
    else:
        print("Error. Password doesn't match. Account locked.")

  def displayBalance(self):
    print(f"""Account Name: {self.accountName}
PIN code: {self.PIN}
Balance: {self.balance}""")
    print("Connected Kiddie Account(s): ")
    total_kiddieAccs = len(self.kiddieAccs)
    for i in range(1,total_kiddieAccs):
        print(f"{self.kiddieAccs[i].accountName}")

  def resetPassword(self):
      password = int(input(f'Enter previous password for {self.accountName}: '))
      if self.PIN == password:
        newpassword = int(input(f"Enter new password for {self.accountName}: "))
        if newpassword > 9999 or newpassword <999:
          print("Error. Password isn't 4 digits. Please try again.")
          self.resetPassword(self)
        else:
          print("PIN code succesfully changed.")
          self.PIN = newpassword
          return self.PIN
      else:
          print("Error. Password doesn't match.")
          return self.PIN

  def deposit(self,amount):
      self.balance += amount
      self.displayBalance()
      return self.balance

  def withdraw(self,amount):
      if amount < self.balance:
        self.balance -= amount
        print(f"Successfully withdrew {amount} from your account.")
        self.displayBalance()
      else:
          print("Error. Amount is larger than balance.")
          pass
      return self.balance
  def connect_kidAcc(self,kiddieAccs):
      self.kiddieAccs.append(kidAcc)
      return self.kiddieAccs

class kidAcc(savingsAccount):
    def __init__(self,accountName,PIN,transferLimit,balance,parentAcc):
        self.accountName = str(accountName)
        self.PIN = int(PIN)
        self.transferLimit = float(transferLimit)
        self.balance = float(balance)
        self.parentAcc = savingsAccount
        
    def receive(self,amount,savingsAccount):
        if amount <= self.transferLimit:
            self.balance += amount
            savingsAccount.balance -= amount
        else:
            print("Amount exceeds transfer limit.")
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount <= self.transferLimit:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Succesfully withdrew {amount} from this account.")
        else:
            print("Amount exceeds transfer limit.")


account1 = savingsAccount("Shelsy",2704,8172011.00, [])
sAcc1 = kidAcc("Eofie",1215,100.00,12000.00,account1)

def adding_secAcc(ba):                                        #sa=Secondary Account
    sa = int(input(f"""Welcome {ba.accountName}!
001 Eofie

Please select a kiddie account to connect to your account: """))
    if sa == 1:
        sa = sAcc1
        if sa.code():
            savingsAccount.connect_kidAcc(ba,sa)
            print("Displaying account information...")
            savingsAccount.displayBalance(ba)
            print(f"""Account Name: {sa.accountName}
        Transfer Limit: {sa.transferLimit}
        Current Balance: {sa.balance}""")
            amount = float(input("Enter the amount you would like to transfer to the all added secondary account: "))
            sa.receive(amount,ba)
            total_secAccs = len(ba.kiddieAccs)
            ba.balance -= amount*total_secAccs
        else:
            sys.exit(0)
    else:
        print("Invalid account number... Displaying information.")
    print(f"""Parent Account Name: {ba.accountName}
Current Balance: {ba.balance}
Kiddie Account Name: {sa.accountName}
Transfer Limit: {sa.transferLimit}
Current Balance: {sa.balance}""")
    sys.exit(0)
        


ba = int(input(f"""Welcome {account1.accountName}!
001 Shelsy

Enter your bank account number: """))
if ba == 1:
    ba = account1
    ba = account1
    ba.code()
    adding_secAcc(ba)
else:
    print("Invalid account number..")
