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


account1 = bankAccount("Shelsy","debit",2704,8172011.00)
account2 = bankAccount("Quiel","debit",4014,1000000.00)

bankAccount.displayBalance(account1)
print("\n")
bankAccount.displayBalance(account2)
print("\n")

account1.PIN = account1.resetPassword()

print("\n")
bankAccount.displayBalance(account1)
print("\n")
bankAccount.displayBalance(account2)

#note: the private attribute PIN wasn't set as a private attribute to allow public display for the demonstration of the process
