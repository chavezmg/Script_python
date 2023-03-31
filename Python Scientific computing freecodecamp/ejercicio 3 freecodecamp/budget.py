class Category:
  
    def __init__(self, name):
        self.name = name.lower().capitalize()
        self.ledger = []
        self.funds = 0
        self.spendings = 0
    
    def __str__(self):
        asterisc = int((30 - len(self.name))/2)
        top = "*" * asterisc + self.name.capitalize() + "*" * asterisc
        ticket = ""
        ticket += top + "\n"
        ticket = list(ticket)
        for line in self.ledger:
            cantidad = "{:.2f}".format(line["amount"])
            long_amount = len(cantidad[:7])
            ticket.append(line["description"][:(23-len(cantidad[6:7]))]) # 22
            long_descrip = len(line["description"][:23])
            ticket.append((" "*(29-(long_descrip+long_amount)) + " " + str(cantidad)[:7] + "\n")) # " "
        ticket.append("Total: " + str("{:.2f}".format(self.get_balance())))
        ticket = "".join(ticket)
        return ticket

    def deposit(self, amount, description=""):
        self.funds += amount
        self.ledger.append({"amount":amount, "description":description})

    def withdraw(self, amount, description=""):
        if self.funds >= amount:
            self.funds -= amount
            self.ledger.append({"amount":-amount, "description":description})
            self.spendings += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.funds

    def transfer(self, amount, name):
        if (self.withdraw(amount, description=f"Transfer to {name.name.capitalize()}")):
            name.deposit(amount, description=f"Transfer from {self.name.capitalize()}")
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True
        
def create_spend_chart(categorias):
    total = 0
    #elements for drawing the ticket
    top = "Percentage spent by category"
    line = "   -----------"
    percentlist = ["100|"," 90|"," 80|"," 70|"," 60|"," 50|"," 40|"," 30|"," 20|"," 10|","  0|"]
    tickettop = []
    ticketbottom = []
    ticket = ""
    bars = []
    bars1= []
    bars2= []
    bars3= []
    #######
    for categoria in categorias:
        total += categoria.spendings
    for categoria in categorias:
        bar = int((categoria.spendings * 100) / (10*total)) + 1
        white_spaces = " " * (11-bar)
        bars.append(white_spaces + "o"*bar + str(categoria.name))
        
    bars1 = bars[0][:11]
    bars2 = bars[1][:11]
    bars3 = bars[2][:11]
    maximo = max(len(bars[0][11:]), len(bars[1][11:]), len(bars[2][11:]))
    tickettop.append(top)
    for element in range(11):
        tickettop.append(percentlist[element] + " " + bars1[element] + "  " + bars2[element] + "  " + bars3[element])
    tickettop.append(line)
    
    bars1 = bars[0][11:] + " "*(maximo-len(bars[0][11:]))
    bars2 = bars[1][11:] + " "*(maximo-len(bars[1][11:]))
    bars3 = bars[2][11:] + " "*(maximo-len(bars[2][11:]))
    iter = 0
    for element in tickettop:
        iter += 1
        #print(element)
        if iter < len(tickettop):
            ticket += f'{"".join(element)}\n'
        else:
            ticket += f'{"".join(element)}'
    for element in range(maximo):
        ticketbottom.append("     " + bars1[element] + "  " + bars2[element] + "  " + bars3[element] + "  ")
    for element in ticketbottom:
        #print(element)
        ticket += f'\n{"".join(element)}'

    return ticket



business = Category("business")
food = Category("food")
entertainment = Category("entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)


print(create_spend_chart([business, food, entertainment]))
print(entertainment.name)