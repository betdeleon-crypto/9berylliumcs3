class bankAccount:
  def __init__(bankAccount, accountName, paymentNetwork, PIN, balance):
    bankAccount.accountName = accountName
    bankAccount.paymentNetwork = paymentNetwork
    bankAccount.PIN = PIN
    bankAccount.balance = balance

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
Balance: {bankAccount.balance}""")

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
    def receive(amount):
        if amount <= secondaryAccount.transferLimit:
            secondaryAccount.balance += amount
        else:
            print("Amount exceeds transfer limit.")
        return secondaryAccount.balance
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

account1 = bankAccount("Shelsy","debit",2704,8172011.00)
account2 = bankAccount("Quiel","debit",4014,1000000.00)
sAcc1 = secondaryAccount("Eofie",1215,True,12000.00,909)
