customerCount = int(input("Enter number of customers : "))

for round in range(1, customerCount + 1):
    print(f"Enter details for Customers {round}")
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    roomNum = int(input("How many rooms would you like to book? : "))
    check = input("Are you staying with pets? (yes/no) : ")

    if check == "yes":
        petCount = int(input("How many pets are you staying with? : "))
    else:
        petCount = 0

    print("\n---Hotel booking Summary---")
    print(f"Name : \t\t\t{name}")
    print(f"Age : \t\t\t{age}")
    print(f"Number of room : \t\t{roomNum}")
    print(f"Staying with pets : \t{check}")
    print(f"Number of pets : {0 + petCount}")

    print(f"\nPet charge : \t\t\t{petCount * 500:,.2f}\tBath")
    print(f"Room charge \t\t\t{roomNum * 1000:,.2f}\tBath")
    print(f"Total charge : \t\t\t{(petCount * 500) + (roomNum * 1000):,.2f}\tBath\n")


