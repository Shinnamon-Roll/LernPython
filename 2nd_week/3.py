elecBill = float(input("Enter your Elec bill : "))
result = 0

if elecBill <= 150:
    result += elecBill * 3.2484

if elecBill > 150 and elecBill <= 400:
    result += ((elecBill - 150) * 4.2218) + (150  * 3.2484)

if elecBill > 400:
    result += ((elecBill - 400) * 4.2218 ) + (150  * 3.2484) + (250 * 4.2218)

print(f"The result is : {result:,.2f} THB.")