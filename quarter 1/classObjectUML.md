# SG4 - Understanding Classes and Objects
## Class Name: Bank Account
## Class Description: Digital storage system that completes transactions similar to a banking system. It consists and uses the stored money from a primary account holder.
## Properties

| Property | Data Type | Description |
| --- | --- | --- |
| Account Name | str | Name of the primary account holder |
| Payment Network | str | Indicates if all transactions will be in **debit** or **credit** |
| PIN | int | Personal identification number or the account password |
| Balance | float | Stores the total money the account holds. |

## Methods:
| Method | Description |
| --- | --- |
| displayBalance() | Displays the current total balance the account stores. |
| deposit(amount: float) | Stores more money to the current balance. |
| withdraw(amount: float) | Takes out money from the current balance. |

## Class Diagram
!![Class Diagram](insert link)

## Design Explanation
### Why did you choose this class?
I chose this class because I have an interest in learning bank processes and transactions, especially those involving bank accounts.

### Which property is the most important? Why?
Out of all properties I listed, the most important is the *balance* property. The primary function of a bank account is to store money. Without a variable to store the money, the bank account wouldn't have a particularly significant use.

### Which method is the most useful? Why?
