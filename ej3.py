class Category: 
    def __init__(self, name):
        self.name = name
        self.ledger = list()
      

    def deposit (self, amount, description = ""):
        self.amount = amount
        self.description = description
        self.ledger.append ({"amount": amount, "description" : description})

#    def withdraw (self, amount, description = ""):
#         self.amount = amount
#         self.description = description

    def transfer(self, amount, category):
        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def get_balance(self)

    totalCash= 0
    for item in self.ledger:
        totalCash += item["amount"]

    return totalCash

    def check_funds(self, amount):
        if(self.get.balance()>= amount)
          return True
    return False
        


