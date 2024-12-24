hours = int(input("Enter a parking time: "))
fee = 0

if hours <= 2:
    print("No fee bro!")

elif 3 <= hours <= 10:
    fee = (hours - 2) * 20
    print(f"The total parking fee is: {fee:,.2f} Bath.")

elif 11 <= hours <= 24:
    fee = (8 * 30) + ((hours - 10) * 25)
    print(f"The total parking fee is: {fee:,.2f} Bath.")

else:
    full_days = hours // 24
    remaining_hours = hours % 24
    fee = full_days * 300 

    if remaining_hours <= 2:
        pass
    elif 3 <= remaining_hours <= 10:
        fee += (remaining_hours - 2) * 20
    elif 11 <= remaining_hours <= 24:
        fee += (8 * 30) + ((remaining_hours - 10) * 25)

    print(f"The total parking fee is: {fee:,.2f} Bath.")
