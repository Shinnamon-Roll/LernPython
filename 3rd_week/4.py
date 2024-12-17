em = int(input("Enter number of employees : "))
count = 1
total = 0
min = 0
max = 0

while count <= em:
    nameEm = input(f"Enter employee name of [{count}] : ")
    salary = int(input("Enter employee Salary : "))
    total += salary
    count += 1

    if max < salary:
        max = salary

    if min > salary or min == 0:
        min = salary

print(f"Total salary : {total:,}")
print(f"Average Salary : {total / em:,.2f}")
print(f"Max salary is : {max}")
print(f"Min salary is : {min}")