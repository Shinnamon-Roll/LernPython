salary = int(input("Enter your salary : "))
years = int(input("Enter year of service : "))

if years > 5:
    bonus = salary * 0.05
    print(f"Bonus is : {bonus:,.2f}")
else:
    print("No bonus")

print(f"Total of salary is : {bonus + salary:,.2f}")