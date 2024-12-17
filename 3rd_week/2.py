firstSide = int(input("Enter first side : "))
secondSide = int(input("Enter second side : "))
thirdSide = int(input("Enter third side : "))

if firstSide + secondSide <= thirdSide or secondSide + thirdSide <= firstSide or thirdSide + firstSide <= secondSide:
    print("Invalid Triangle")
    
elif firstSide == secondSide == thirdSide:
    print("Equilateral Triangle")

elif firstSide == secondSide or secondSide == thirdSide or thirdSide == firstSide:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")
