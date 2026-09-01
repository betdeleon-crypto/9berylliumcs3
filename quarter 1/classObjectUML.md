# My OOP Seed System
**Class Name:** Bank Account

**Description:** Digital storage system that completes transactions similar to a banking system. It consists and uses the stored money from a primary account holder.

**Property:**
| Property | Data Type | Description |
| --- | --- | --- |
| Account Name | str | Name of the primary account holder |
| Payment Network | str | Indicates if all transactions will be in **debit** or **credit** |
| PIN | int | Personal identification number or the account password |
| Balance | float | Stores the total money the account holds. |

**Methods:**
| Method | Description |
| --- | --- |
| displayBalance() | Displays the current total balance the account stores. |
| deposit(amount: float) | Stores more money to the current balance. |
| withdraw(amount: float) | Takes out money from the current balance. |
