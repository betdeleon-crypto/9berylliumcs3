# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](https://github.com/betdeleon-crypto/9berylliumcs3/blob/19548fc76d03b4cefee11aa9ddb9643b0c576b4d/quarter%201/classObjectUML.md)

[Part II - Class Attributes and Methods](https://github.com/betdeleon-crypto/9berylliumcs3/blob/19548fc76d03b4cefee11aa9ddb9643b0c576b4d/quarter%201/classAttributesMethods.md)

## Existing Class
Class: __Bank Account__

Description: A software storage system where simple banking processes are performed. Information included here are the personal details of the primary account holder and their current bank balance.

## New Related Class
Class: __Secondary Bank Account__

Description: Similar to the Bank Account class, the Secondary class allows for simple banking processes to be performed. 
It comprises the details of a secondary account holder and allows for easier bank processes involving both accounts.

## Association
Relationship: A bank account may be linked to a secondary account, while a secondary account is always connected to a primary bank account.

Explanation:
## Multiplicity
Multiplicity: One-to-Many

Explanation: Bank accounts are best used when the feature to add secondary accounts are in service. This is especially used by couples, groups of friends, and families.

## UML Class Relationship Diagram
![Class Relationship Diagram](https://github.com/betdeleon-crypto/9berylliumcs3/blob/fc828a871be8096e5ddf35c9f6d780ed4521f4c5/quarter%201/images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](https://github.com/betdeleon-crypto/9berylliumcs3/blob/ecbd7d1211c8d8ae86157a4a7eb38ca0faee76fb/quarter%201/classRelationships.py)

## Test Run
![Relationship Test Run](https://github.com/betdeleon-crypto/9berylliumcs3/blob/571ada5155dd2862ef931c6b52bdf5f459abe849/quarter%201/images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](https://github.com/betdeleon-crypto/9berylliumcs3/blob/bcbd77f56c7a7d6d8b603e7b2b7cc35bb2d6975c/quarter%201/images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
Between bank accounts and secondary accounts, they display a one-to-many association. Bank accounts are best used when there are secondary accounts linked to it. It allows for financial collaboration and supervision over the secondary account, something like parent control mode.

### What multiplicity did you choose and why?
A bank account can have zero or many multiplicities. Bank account owners have the option to link their account with multiple secondary accounts, or to simply use it without any links. This option is influenced by their personal situation. For instance, parents would most likely link their account to their children's accounts, while others may opt to keep their primary account as it is.

### How did you implement the relationship in Python?
The implementation was a challenging process of trial and error, and careful comprehension and consideration of their relationship. It became easier when I was able to understand that bank accounts may have zero or many relationships. Additionally,

### Why did you store an object reference instead of copying its data?
Storing an object reference allows the bank account to easily access the secondary account(s). It avoids duplication and helps to create separate variables which store information. In this way, the program runs smoothly and efficiently.

### If your relationship uses many, why is a list appropriate?
A list is essential to keep track of the possibly many secondary accounts each bank account has. Because of their one-to-many association, it's important to track the different accounts linked to each other. It organizes information for easier use.
