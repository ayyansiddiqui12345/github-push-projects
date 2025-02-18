class BikeShop: 
    def __init__(self, stock):
        self.stock = stock

    def display_bikes(self):
        print("Total bikes:", self.stock)

    def rent_a_bike(self, q):
        if q <= 0:
            print("Enter a positive value greater than zero.")
        elif q > self.stock:
            print(f"Not enough bikes in stock. Available bikes: {self.stock}")
        else:
            self.stock -= q
            print(f"Total Price: {q * 100}")
            print(f"Total Bikes left: {self.stock}")

# Create the bike shop object with an initial stock of 100 bikes
obj = BikeShop(100)

while True:
    # Display menu options
    uc = int(input('''
    1 Display Stocks
    2 Rent a Bike
    3 Exit            
    '''))

    if uc == 1:
        obj.display_bikes()
    elif uc == 2:
        # Get number of bikes user wants to rent
        q = int(input("Enter the number of bikes you want to rent: "))
        obj.rent_a_bike(q)  # Call the method to rent bikes
    elif uc == 3:
        print("Exiting the program. Thank you for using our service!")
        break
    else:
        print("Invalid option. Please choose a valid option.")