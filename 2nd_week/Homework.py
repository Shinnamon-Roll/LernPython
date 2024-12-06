def main():
    while True:
        choice = input("Do you want to calculate (y / n) : ")
        
        if choice == "y":
            p = int(input("Enter the loan amount : "))
            r = float(input("Enter the annual interest rate (in %) : "))
            n = int(input("Enter the number of years to pay off the loan : "))

            r, n = convert(r, n)
            calculate(p, r, n)
            
        else:
            print("Exiting Program...")
            break

def convert(r, n):
    r = r / 12 / 100
    n = n * 12

    return r, n

def calculate(p, r, n): 
    monthlyInstallment = (p * r * (( 1 + r ) ** n)) / ((( 1 + r ) ** n ) - 1)

    print(f"The monthly installment is : {monthlyInstallment:,.2f}")
    print(f"The total interest paid is : {(monthlyInstallment * n) - p:,.2f}")

main()