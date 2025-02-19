class bikeshop:
    def __init__(self, stock):
        self.stock = stock
    def displaybikes(self):
        print("Total bikes", self.stock)
    def rentforbike(self, q):
        
        if q<=0:
            
            print("Enter the positive value greater than zero")
        if  q>self.stock:
            print("please enter the value less than stock")
            
        else :
            self.stock = self.stock -q
            print("Total Price ", q*100)
            print("total bikes", self.stock)
while True:
    obj = bikeshop(100)
    uc = int(input(""" 
                   1. display stock
                   2. Rent a bike
                   3. Exit.
                   """))
    if uc ==1:
        obj.displaybikes()
    elif uc==2:
        n=int(input("Enter the quantity"))
        obj.rentforbike(n)
    else:
        break
        
    