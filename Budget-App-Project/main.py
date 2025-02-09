class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        object = {'amount': amount, 'description': description}
        self.ledger.append(object)
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            object = {'amount': -amount, 'description': description}
            self.ledger.append(object)
            return True
        else:
            return False

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category): 
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else: 
            return False
          
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            items += description + amount + "\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total  

def create_spend_chart(categories):

    category_spent = [ -sum (entry['amount'] for entry in category.ledger if entry['amount'] < 0) for category in categories]

    total_spent = sum(category_spent)

    category_percentage = [(spent / total_spent *100)// 10  for spent in category_spent]

    chart = "Percentage spent by category\n"

    for i in range (100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in category_percentage:
            if percentage >= i/10:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += '    ' + '-'*(len(categories)*3 + 1) + '\n'
    
    length = max(len(category.name) for category in categories)
    
    category_names = [category.name.ljust(length) for category in categories]

    for i in range(length):
        if i != length - 1: 
            chart += "     " + "".join(category_name[i] + "  " for category_name in category_names) + "\n"
        else:
            chart += "     " + "".join(category_name[i] + "  " for category_name in category_names)

    return chart
  
# Execution : 
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "Initial deposit")
food.withdraw(105.55, "Groceries")
food.withdraw(30, "Restaurant")

clothing.deposit(500, "Initial deposit")
clothing.withdraw(50, "Jeans")

entertainment.deposit(200, "Initial deposit")
entertainment.withdraw(75, "Movies")

print(create_spend_chart([food, clothing, entertainment]))
