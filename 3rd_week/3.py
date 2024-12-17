first = int(input("Enter the first number : "))
second = int(input("Enter the second number : "))
third = int(input("Enter the third number : "))

num1, num2, num3 = 0, 0, 0

if num1 < first:
    num1 = first

if num1 < second:
    num2 = num1 
    num1 = second

if num1 < third:
    num3 = num2
    num2 = num1
    num1 = third

print(f"{num1} {num2} {num3}")