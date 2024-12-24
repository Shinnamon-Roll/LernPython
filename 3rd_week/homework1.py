print("Welcome to the Fuel Station!")

print("Choose your fuel type:")
print("1. Petrol \n2. Diesel \n\nOr press q for exit")

while True:
    choice = input("Enter your choice (1 or 2 or q): ")

    if choice.lower() == 'q':
        break
    
    if choice == 1:
        quantity = int(input("Enter the quantity of fuel in liters : "))
        print(f"Cost for {quantity} liters of petrol is {quantity * 35.9:,.2f}")

    elif choice == 2:
        quantity = int(input("Enter the quantity of fuel in liters : "))
        print(f"Cost for {quantity} liters of diesel is {quantity * 29.6:,.2f}")

    else:
        print("Invalid choice!")
        pass

