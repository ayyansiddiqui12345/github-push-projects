
class calculator:
    def __init__(self):
        pass
    def add(self, a,b):
        return a+b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    
    
if __name__ == "__main__":
    calc = calculator()
    print("Simple Calculator Using OOP")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("\nEnter your choice (1/2/3/4) or 'q: ")
        if choice == 'q':
            print("Goodbye!")
            break
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if choice == '1':
                print(f"Result: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {calc.divide(num1, num2)}")
            else:
                print("Invalid choice. Please select a valid option.")
        