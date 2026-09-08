#method renew password added

class bankAccount:
  def __init__(bankAccount, accountName, paymentNetwork, PIN, balance):
    bankAccount.attribute1 = accountName
    bankAccount.attribute2 = paymentNetwork
    bankAccount.__attribute3 = PIN
    bankAccount.__attribute4 = balance

  def displayBalance(bankAccount):
    code = int(input(f"Enter password for {bankAccount.accountName}: "))
    if code == bankAccount.PIN:
        print(f"""Account Name: {bankAccount.accountName}
        Balance: {bankAccount.balance}""")

  def resetPassword(bankAccount):
      password = int(input('Enter previous password: '))
      if bankAccount.PIN == password:
        password = int(input("Enter new password: "))
        if password > 9999 or password <999:
          print("Error. Password isn't 4 digits. Please try again")
          bankAccount.resetPassword(bankAccount)
        else:
          return password

  def deposit(bankAccount,amount):
      bankAccount.balance += amount
      return bankAccount.balance

  def withdraw(bankAccount,amount):
      if amount > bankAccount.balance:
        bankAccount.balance -= amount
      else:
          print("Error. Amount is larger than balance.")
          bankAccount.withdraw(bankAccount,amount)
      return bankAccount.balance
      
account1 = bankAccount("Eofie","debit",1215,6677.67)

def interface():
  n = int(input("""1 Withdraw
2 Deposit
3 Reset Password
4 Display Balance

Enter the number of your next step: """))
  if n == 1:
    amount = float(input("Enter the amount you will withdraw: "))
    bankAccount.balance = bankAccount.withdraw(account1,amount)
  elif n == 2:
    amount = float(input("Enter the amount you will deposit: "))
    account1.balance = bankAccount.deposit(account1,amount)
  elif n == 3:
    account1.PIN = account1.resetPassword(account1)
  elif n == 4:
    bankAccount.displayBalance(account1)
  else:
    print("Error. Please input a valid step.")
    interface()
    
interface()

'''Your methods must satisfy all of these requirements:
At least one method receives a parameter.
At least one method changes an attribute.
At least one method reads or returns information about the object.
At least one method must safely interact with a private attribute.'''
