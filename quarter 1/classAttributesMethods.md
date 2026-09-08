# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/betdeleon-crypto/9berylliumcs3/blob/5b18f2495b56ce2e2ce0b960ff1152141bbf7251/quarter%201/classObjectUML.md)

## Design Revision
Two new methods for the class Bank Account were added; the code method and reset password method. The code method will verify the user's identity with the account they will be accessing, while the reset password method allows the verified user to change their bank account's PIN code.

## Visibility Decisions

| Attribute | Data Type | Visibility | Reason |
| --- | --- | --- | --- |
| Account Name | str | public | Real names are used to identify various accounts and to keep track of transaction records. |
| PIN Code | int | private | To verify the account user's identity and to protect account usage from unauthorized access. |
| Payment Network | str | public | It identifies the payment network that will be used. |
| Balance | float | public | Account balance can be viewed to manage operations or offer service and products. |

## Updated UML Class Diagram
![Class Diagram](--)

## Python Implementation

[View Python Source](https://github.com/betdeleon-crypto/9berylliumcs3/blob/5b18f2495b56ce2e2ce0b960ff1152141bbf7251/quarter%201/classImplementation.py)

## Test Run
![Test Run](https://github.com/betdeleon-crypto/9berylliumcs3/blob/bedffb880e430d0d3ae0d0534f53c55470a95da9/quarter%201/images/classTestRun.png)

## Object Diagram
![Object Diagram](--)

## Analysis

### Why did you make your chosen attribute private?

### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
