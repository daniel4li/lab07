from Pizza import Pizza

class CustomPizza(Pizza):
   
    def __init__ (self,size):
        self.size = size
        self.topping  = []
        if size == "S": 
            self.price = 8.00
        elif size == "M":
            self.price = 10.00
        else:
            self.price = 12.00
        


    def addTopping(self, topping):
        self.topping.append(topping)
        if self.size == "S": 
            self.price += 0.50
        elif self.size == "M":
            self.price += 0.75
        else:
            self.price += 1.00

    def getPizzaDetails(self):
        a = "CUSTOM PIZZA" + "\n" + "Size: " + str(self.size) + "\n" 
        b = "Toppings:" + "\n"
        for i in self.topping:
            c = "\t" + "+ " + i + "\n"
            
            b = b + c
        d = "Price: $" + str("{0:.2f}".format(self.price, 2)) + "\n"
        return a + b + d


