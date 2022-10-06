class Category: 
    def __init__(self, name):
        self.name = name
        self.ledger = list()
      

    def deposit (self, amount, description = ""):
        self.ledger.append ({"amount": amount, "description" : description})

    def withdraw (self, amount, description = ""):
        if(self.check_funds(amount)):
          self.ledger.append ({"amount": -amount, "description" : description})
          return True
        return False

    def transfer(self, amount, category):
        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def get_balance(self):

        totalCash= 0
        for item in self.ledger:
          totalCash += item["amount"]

        return totalCash

    def check_funds(self, amount):
        if(self.get_balance() >= amount):
          return True
        return False


    def __str__(self): 
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output
 
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())




print(food)