# Advanced Class Relationships
## Previous Activities
[classAttrib](https://github.com/betdeleon-crypto/9berylliumcs3/blob/7ecffab88613355adbb75483664d1a2f74eb28fa/quarter%201/classAttributesMethods.md)

[classRel](https://github.com/betdeleon-crypto/9berylliumcs3/blob/7ecffab88613355adbb75483664d1a2f74eb28fa/quarter%201/classRelationships.md)

## Existing System Description:
The existing system involved a primary bank account and a secondary bank account, with the holder of the primary account having more 
control over the secondary bank account, somewhat similar to the concept of parental control. In my previous design, there were various 
repeated attributes and methods between the two associated classes, and their relationship was a bit too unclear and vague. The system 
must be modified to make the secondary class more specific. 

## Inheritance Relationship
Parent: Bank Account
Child: Kiddie Bank Account
Explanation: The kiddie bank account is a type of bank account where it has more restrictions, limitations and conditions for the 
holder of the kiddie account. Additionally, it may act as a secondary account to the parent bank account, allowing the parent to have 
easier control and access to the account.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship:

Explanation:

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
### What is the difference between Association from Part III and the advanced relationship you implemented?
### How does your design follow the DRY principle?
