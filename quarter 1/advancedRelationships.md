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
Parent: Savings Bank Account

Child: Kiddie Bank Account

Explanation: The kiddie bank account is a type of bank account where it has more restrictions, limitations and conditions for the 
holder of the kiddie account. Additionally, it may act as a secondary account to the parent bank account, allowing the parent to have 
easier control and access to the account.

## Inheritance UML
![Inheritance](https://github.com/betdeleon-crypto/9berylliumcs3/blob/ae93e4c66c3c7dfc478a38cd1878d16f9eb9c631/quarter%201/images/inheritanceDiagram)

## Composition/Aggregation
Relationship: Composition

Explanation: A savings account can exist without a kiddie account, but a kiddie account cannot exist without a parent savings account. 
Minors cannot hold legal bank accounts without any parental guidance. Additionally, the kiddie bank account serves as another asset 
the parent savings account legally owns and controls.

## Advanced UML Diagram
![Advanced UML](https://github.com/betdeleon-crypto/9berylliumcs3/blob/ab5b438d0d70ea1c3a5b078dfd4906e46a003ea3/quarter%201/images/advancedClassDiagram)

## Python Implementation
[Source Code](https://github.com/betdeleon-crypto/9berylliumcs3/blob/546fb170c83a22adbd100d04eb314621749ee4f2/quarter%201/advancedRelationships.py)

## Test Run
![Test](https://github.com/betdeleon-crypto/9berylliumcs3/blob/aa5679a7c6cfc035ea994cb6fce3d5ce88745294/quarter%201/images/advancedTestRun)

## Object Diagram
![Objects](https://github.com/betdeleon-crypto/9berylliumcs3/blob/546fb170c83a22adbd100d04eb314621749ee4f2/quarter%201/images/advancedObjectDiagram)

## Reflection
### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
The child class kid account is a type of specialized savings bank account. Inheritance relationship works well on this model because 
it allows the owner of the parent account to have control over the child's account while still maintaining some normal functions a 
typical savings account would perform such as deposit and reset password. This kind of model would also work well with other similar 
functions and activities including hierarchy.

### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance in code helped reduce duplicate code through a similar concept as the use of functions. In my program, methods such as 
withdraw, deposit, reset password, and code were all inherited by the kid account class. It made my code look cleaner and became 
easier to understand.

### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
My two objects have a composition type of HAS-A relationship. The parent object, savings account, can exist without any connected 
secondary kid account, while the kid account must have a connected parent account for it to exist. This relationship is based on my 
idea and logic on the mini program I created. 

### What is the difference between Association from Part III and the advanced relationship you implemented?
The association from the previous activity served as the foundation to the concept and implementation of advanced relationships. 
It helped me understand that two classes can be linked, while the concept of advanced relationships strengthened my idea through 
introducing a more convenient way to link these objects.

### How does your design follow the DRY principle?
This design follows the principle of Dont Repeat Yourself through reusing methods and extending logic. Instead of rewriting similar 
methods and attributes, the logic in this design allows for inheritance of methods and attributes, allowing the child class to 
reuse the inherited traits. Additionally, the logic used in the methods of the parent class was applicable to the child class, showing 
how logic could be extended.
