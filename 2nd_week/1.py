balance = 0
while True:
    choice = input("What do you want to do (dept or width) : ")

    if choice == "dept":
        dept = float(input("Enter the amount to deposit : "))
        balance -= dept
        print(f"your dept is : {dept:.2f}, Your new balance is : {balance:.2f}")

    elif choice == "width":
        width = float(input("Enter the amount to widthdraw : "))
        balance += width
        print(f"your dept is : {width:.2f}, Your new balance is : {balance:.2f}")
    else:
        break