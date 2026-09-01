# SG4 - Understanding Classes and Objects
## Class Name: Bank Account
## Class Description: Digital storage system that completes transactions similar to a banking system. It consists and uses the stored money from a primary account holder.
## Properties

| Property | Data Type | Description |
| --- | --- | --- |
| Account Name | str | Name of the primary account holder |
| Payment Network | boolean | Indicates if all transactions will be in **debit** or not. |
| PIN | int | Personal identification number or the account password |
| Balance | float | Stores the total money the account holds. |

## Methods:
| Method | Description |
| --- | --- |
| displayBalance() | Displays the current total balance the account stores. |
| deposit(amount: float) | Stores more money to the current balance. |
| withdraw(amount: float) | Takes out money from the current balance. |

## Class Diagram
![Class Diagram](https://github.com/betdeleon-crypto/9berylliumcs3/blob/edc574c8b8ad0b8d382f3981d53667c5d4798004/quarter%201/images/UML%20Class%20Diagram.jpg)

## Design Explanation
### Why did you choose this class?
I chose this class because the process of learning bank transactions involving bank accounts holds a special place in my heart and life. Ever since I entered Pisay, my mother started to teach me the system of such procedures, which sparked a keen interest in banking within me.

### Which property is the most important? Why?
Out of all properties I listed, the most important is the *balance* property. The primary function of a bank account is to store money. Without a variable to store the money, the bank account wouldn't have a particularly significant use other than to keep personal information, which doesn't give it any extra distinctiveness from other methods.

### Which method is the most useful? Why?
The *displayBalance* method is arguably the most valuable amongst all other methods because it is the fundamental step which helps us track the amount of the remaining money in the account. It helps us be aware and updated of the current funds on deposit of the account holder. From this, we will be able to budget our money more properly and efficiently, 


