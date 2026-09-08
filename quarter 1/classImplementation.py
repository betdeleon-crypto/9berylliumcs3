#method renew password added

class bankAccount:
  def __init__(bankAccount, accountName, paymentNetwork, PIN, balance):
    bankAccount.accountName = accountName
    bankAccount.paymentNetwork = paymentNetwork
    bankAccount.__PIN = PIN
    bankAccount.__balance = balance

  def displayBalance(bankAccount):
    code = int(input(f"Enter password for {bankAccount.accountName}: "))
    if code == bankAccount.__PIN:
        print(f"""Account Name: {bankAccount.accountName}
Balance: {bankAccount.__balance}""")

  def resetPassword(bankAccount):
      password = int(input('Enter previous password: '))
      if bankAccount.__PIN == password:
        password = int(input("Enter new password: "))
        if password > 9999 or password <999:
          print("Error. Password isn't 4 digits. Please try again")
          bankAccount.resetPassword(bankAccount)
        else:
          return password
          print(f"""Account Name: {bankAccount.accountName}
PIN: {bankAccount.__PIN}""")

  def deposit(bankAccount,amount):
      bankAccount.__balance += amount
      return bankAccount.__balance

  def withdraw(bankAccount,amount):
      if amount > bankAccount.__balance:
        bankAccount.__balance -= amount
      else:
          print("Error. Amount is larger than balance.")
          pass
      return bankAccount.__balance
      
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
    account1.__PIN = account1.resetPassword()
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
