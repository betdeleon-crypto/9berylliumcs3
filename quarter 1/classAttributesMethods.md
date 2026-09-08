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
![Class Diagram](https://github.com/betdeleon-crypto/9berylliumcs3/blob/b7d1bb7947c72c829a3edc4b6707d5262e85b4ab/quarter%201/images/classDiagramSG5.png)

## Python Implementation

[View Python Source](https://github.com/betdeleon-crypto/9berylliumcs3/blob/5b18f2495b56ce2e2ce0b960ff1152141bbf7251/quarter%201/classImplementation.py)

## Test Run
![Test Run](https://github.com/betdeleon-crypto/9berylliumcs3/blob/bedffb880e430d0d3ae0d0534f53c55470a95da9/quarter%201/images/classTestRun.png)

## Object Diagram
![Object Diagram](https://github.com/betdeleon-crypto/9berylliumcs3/blob/159ed3b8b55b1f790df52ae2e9abdb5e90ab46e6/quarter%201/images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?
I chose to make the PIN code as a private attribute because I understand that the information contained in this variable should be protected for identity and account protection, especially in real life applications of such information. The PIN code is commonly used in situations similar to this, where identity, when personally and individually confirmed, becomes an incovenient task. To make it practical, PIN codes shouldn't be publicly shared, most particularly to strangers or acquaintances.

### Which method changes the state of your object?
Among all listed methods, the method to reset the PIN code or method resetPassword was the only method that has the ability to change the state of an object. It's essential that the account users have the ability to reset their PIN code, especially when they are doxxed or when they forget their PIN. Additionally, this ability may provide extra security because they will be able to change their PIN more frequently. In short, the ability to change PIN codes allow the users to keep important access over the account conveniently and efficiently while also allowing enhanced account security.

### How did your two objects demonstrate that instances are independent?
When the method was called, changes were observed only on the PIN attribute of the first bank account. The instance displayed independence, particularly when the initial and final values were displayed and the changes were compared. It showed how changing the PIN code of the first object did not affect the final PIN code of the second object.

### What is the difference between your class diagram and your object diagram?
I'd like to think of my class diagram as the basic and my object diagram as the specifics. My class diagram served as the structure format in which the specifics will follow. It showed the basic structure each object will follow, while the object diagram assigned specific values to each attribute per object.
