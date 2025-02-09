# **Budget-App-Project**

FreeCodeCamp - **Scientific Computing with Python** (Third Project)  

## 📌 **Project Overview**  
The Category class models a budget category (e.g., food, clothing, entertainment) and provides functionality to manage deposits, withdrawals, transfers, and balance tracking.

### Methods:
- **`deposit(amount, description="")`**:
    Adds a deposit entry to the ledger with the specified amount and description (defaults to an empty string).
  
- **`withdraw(amount, description="")`**:
    Adds a withdrawal entry to the ledger (negative amount). If insufficient funds, the withdrawal is not added and `False` is returned; otherwise, `True` is returned.
  
- **`get_balance()`**: Returns the current balance of the category by summing deposits and withdrawals.
- **`transfer(amount, category)`**: Transfers the specified amount from the current category to another. Both categories will have corresponding deposit and withdrawal entries. If there are insufficient funds, no transactions will occur, and `False` will be returned.
- **`check_funds(amount)`**: Checks if the current balance is sufficient for the given amount. Returns `True` if sufficient, `False` otherwise.
  
### Display:

When a Category object is printed, it displays:
- A centered title of the category name (e.g., *************Food*************).
- A ledger list with description (up to 23 characters) and amount (right-aligned with two decimal places).
- The total balance at the bottom.

### Example Usage : 
```sh
food = Category('Food')
food.deposit(1000, 'Initial deposit')
food.withdraw(10.15, 'Groceries')
food.withdraw(15.89, 'Restaurant and dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
```
### Output : 
```sh
*************Food*************
Initial deposit          1000.00
Groceries                -10.15
Restaurant and dessert   -15.89
Transfer to Clothing     -50.00
Total: 923.96
```

### `create_spend_chart(categories)`:
-  This function generates a bar chart to visualize the percentage of funds spent in each category.
-  Takes a list of Category objects.
-  Displays a chart with percentages calculated from withdrawals.
-  Each category’s bar is represented by 'o' characters, with vertical labels showing percentages.
-  A title "Percentage spent by category" is displayed at the top.

### Example Output:
```sh
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g
```
