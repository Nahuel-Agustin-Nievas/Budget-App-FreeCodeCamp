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


    def spent(self):
        b = 0
        for t in self.ledger:
            amount = t["amount"]
            if amount < 0:
                b += amount

        return -b


def create_spend_chart(categories):
    spending = [c.spent() for c in categories]
    total = sum(spending)
    percentages = [s * 100 / total for s in spending]
    ss = ["Percentage spent by category"]
    for i in range(0, 11):
      level = 10 * (10 - i)
      s = '{:>3}| '.format(level)
      for p in percentages:
        if p >= level:
            s += "o  "
        else:
            s += "   "
      ss.append(s)
    padding = " " * 4
    ss.append(padding + "-" * 3 * len(spending) + "-")

    names = [c.name for c in categories]
    n = max(map(len, names))
    for i in range(0, n):
        s = padding
        for name in names:
          s += " "
          s += name[i] if len(name) > i else " "
          s += " " 

        
        ss.append(s + " ")

    return "\n".join(ss)

        
 
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())




print(food)