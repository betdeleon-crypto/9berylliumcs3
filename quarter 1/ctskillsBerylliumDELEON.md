#                            Annex B
##  Computational Thinking Exercise: "Smart Vending Machine"
> Name: **Bycalene Eofie T. De Leon**
> Section: **Beryllium**                       
> Date: August 20, 2026
Score: ____________

**Scenario**
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:
* Sometimes the machine does not give the correct change.
* Items run out, but the machine doesn’t notify anyone.
* Students press the wrong buttons and get the wrong item.
* The machine is slow when multiple students use it in succession.

Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

**Step 1**: Identify the Big Problem
Main Problem: The school vending machine provides a slow and inefficient meal service because it doesn't provide the correct change, it is slow when used simultaneously by students, and there is no system for monitoring its food inventory. This causes long queues and overcrowding during lunch break.

**Step 2**: Identify three to four Sub-Problems
Possible sub-problems:
1. `There is no tracking system for food inventory.`
2. `Students may receive incorrect change.`
3. `Item descriptions aren't well defined.`
4. `Inefficient and slow service leads to long queues.`


**Step 3**: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:
| Sub-Problem | CT Skill | Example Solution |
|-------------|----------|------------------|
| There is no tracking system for food inventory. | Decomposition | Create a system that effectively records each food item, its quantity, and subtracts stocks from it when sold. |
| Students may receive incorrect change. | Algorithmic Design | Develop a calculating system that calculates total cost and change after the user enters the amount paid. |
| Item descriptions aren't well defined. | Abstraction | Create a digital menu consisting of short descriptions including only the substantial information per food item. |
| Inefficient and slow service leads to long queues. | Decomposition | Organize a step-by-step process that effectively accomplishes one order. Start from food selection, before proceeding to the calculating and dispensing system. |


**Step 4**: Draw a flowchart or write a pseudocode for the identified sub-problem
1. `Food Inventory Tracking System `
```
display menu
select food item
check available stock
if stock > 0:
  add food item to basket
  ask user if they will add more items
  if user "yes":
      repeat process
  else:
      proceed to checkout
      calculate total cost and change
      ask user if they will proceed
      if user proceeds:
        dispense food item
        dispense change
        display home screen
      else:
        cancel order
else:
  display "Unavailable Stock"
```
   
2. `Calculating System`
```
display menu
select food item
if food item is added to their basket:
  add price value of the item to the total cost
if user proceeds to checkout:
  display total cost
  accept payment amount
  calculate if payment >= total cost
  if payment >= total cost:
    change = payment - total cost
    if change == 0:
      dispense food items
    else:
      dispense food items
      dispense change
else:
  cancel
```


3. `Digital Menu` ; 
   The pseudocode of this example solution will only be applicable when the manager is configuring the machine.
```
enter food item name
enter if item is a beverage or food
enter item description
enter price
enter stock
save item information
display item
```

4. `Organized and Efficient Service Processess`
```
display menu
select food item
check available stock
if stock > 0:
  add food item to basket
  add item price to total cost
  ask user if they will add more items
  if user "yes":
      repeat process
  else:
      display total cost
      accept payment amount
      calculate if payment >= total cost
      if payment >= total cost:
        change = payment - total cost
        if change == 0:
          dispense food items
        else:
          dispense food items
          dispense change
      ask user if they will proceed
      if user proceeds:
        dispense food item
        dispense change
        display home screen
      else:
        cancel order
else:
  display "Unavailable Stock"
```
