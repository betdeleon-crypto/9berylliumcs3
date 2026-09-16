import sys

class bankAccount:
  def __init__(bankAccount, accountName, paymentNetwork, PIN, balance, secondaryAcc):
    bankAccount.accountName = accountName
    bankAccount.paymentNetwork = paymentNetwork
    bankAccount.PIN = PIN
    bankAccount.balance = balance
    bankAccount.secondaryAcc = []

  def code(bankAccount):
    code = int(input(f"Enter password for {bankAccount.accountName}: "))
    if code == bankAccount.PIN:
        return True
    else:
        print("Error. Password doesn't match. Account locked.")

  def displayBalance(bankAccount):
    print(f"""Account Name: {bankAccount.accountName}
PIN code: {bankAccount.PIN}
Payment Network: {bankAccount.paymentNetwork}
Balance: {bankAccount.balance}
Connected Seondary Accounts: {bankAccount.secondaryAcc}""")

  def resetPassword(bankAccount):
      password = int(input(f'Enter previous password for {bankAccount.accountName}: '))
      if bankAccount.PIN == password:
        newpassword = int(input(f"Enter new password for {bankAccount.accountName}: "))
        if newpassword > 9999 or newpassword <999:
          print("Error. Password isn't 4 digits. Please try again.")
          bankAccount.resetPassword(bankAccount)
        else:
          print("PIN code succesfully changed.")
          bankAccount.PIN = newpassword
          return bankAccount.PIN
      else:
          print("Error. Password doesn't match.")
          return bankAccount.PIN

  def deposit(bankAccount,amount):
      bankAccount.balance += amount
      bankAccount.displayBalance()
      return bankAccount.balance

  def withdraw(bankAccount,amount):
      if amount < bankAccount.balance:
        bankAccount.balance -= amount
        print(f"Successfully withdrew {amount} from your account.")
        bankAccount.displayBalance()
      else:
          print("Error. Amount is larger than balance.")
          pass
      return bankAccount.balance
  def add_secAcc(bankAccount,secAcc):
      bankAccount.secondaryAcc.append(secAcc)
      return bankAccount.secondaryAcc

class secondaryAccount:
    def __init__(self,accountName,PIN,status,transferLimit,balance):
        self.accountName = str(accountName)
        self.PIN = int(PIN)
        self.status = status                        #active or not
        self.transferLimit = float(transferLimit)
        self.balance = float(balance)
    def code(secondaryAccount):
        code = int(input(f"Enter password for {secondaryAccount.accountName}: "))
        if code == secondaryAccount.PIN:
            return True
        else:
            print("Error. Password doesn't match. Account locked.")
    def receive(self,amount):
        if amount <= self.transferLimit:
            self.balance += amount
        else:
            print("Amount exceeds transfer limit.")
        return self.balance
    def deposit(amount):
        secondaryAccount.balance += amount
        return secondaryAccount.balance
    def withdraw(amount):
        if amount <= secondaryAccount.balance:
            secondaryAccount.balance -= amount
            print(f"Succesfully withdrew {amount} from this account.")
    def resetPassword():
        password = int(input(f"Enter previous password for {secondaryAccount.accountName}: "))
        if password == secondaryAccount.PIN:
            newpass = int(input(f"Enter new password for {secondaryAccount.accountName}"))
            if newpass > 999 or newpass < 9999:
                secondaryAccount.PIN = newpass
                print("Password succefully changed.")
                return secondaryAccount.PIN
            else:
                print("Error. Password exceeds 4 digits. Please try again.")
        else:
            print("Error. Password doesn't match.")

account1 = bankAccount("Shelsy","debit",2704,8172011.00, [])
account2 = bankAccount("Quiel","debit",4014,1000000.00, [])
sAcc1 = secondaryAccount("Eofie",1215,True,12000.00,909)
sAcc2 = secondaryAccount("Yumi",1003, True, 100.00, 6677)
sAcc3 = secondaryAccount("Krisha", 1808, True, 10000, 10)

accounts = [account1, account2]

def adding_secAcc(ba):                                        #sa=Secondary Account
    sa = int(input(f"""Welcome {ba.accountName}!
    001 Eofie
    002 Yumi
    003 Krisha
Please select a secondary account holder: """))
    if sa == 1:
        sa = sAcc1
        bankAccount.add_secAcc(ba,sa)
    elif sa == 2:
        sa = sAcc2
        bankAccount.add_secAcc(ba,sa)
    elif sa == 3:
        sa = sAcc3
        bankAccount.add_secAcc(ba,sa)
    boo = input("Enter any number to add another secondary account: ")
    try:
        float(boo)
        adding_secAcc(ba)
    except ValueError:
        print("Displaying account information...")
        bankAccount.displayBalance(ba)
        print(f"""Account Name: {sa.accountName}
Transfer Limit: {sa.transferLimit}
Current Balance: {sa.balance}""")
        amount = float(input("Enter the amount you would like to transfer to your secondary account: "))
        sa.receive(amount)
        print(f"""Account Name: {sa.accountName}
Transfer Limit: {sa.transferLimit}
Current Balance: {sa.balance}""")
        sys.exit(0)
        


ba = int(input('''Welcome user!
001 Shelsy
002 Quiel
Please select your account number: '''))
if ba == 1:
    ba = account1
    ba.code()
    adding_secAcc(ba)
elif ba == 2:
    ba = account2
    ba.code()
    adding_secAcc(ba)
else:
    print("Invalid account number. Please try again.")
    sys.exit(0)

