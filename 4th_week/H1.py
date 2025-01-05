person = int(input("Enter number of Person : "))

for count in range(person):
    name = input(f"\nEnter your name {count + 1} : ")
    weight = int(input("Enter your weight : "))
    height = int(input("Enter your height : "))

    bmi = weight / ((height / 100) ** 2)
    print(f"BMI : {bmi:.1f}")

    word = "Your Category of BMI is"

    if bmi < 16:
        print(f"{word} Severe Thinness")
    elif bmi < 17:
        print(f"{word} Moderate Thinness")
    elif bmi < 18.5:
        print(f"{word} Mild Thinness")
    elif bmi < 25:
        print(f"{word} Normal")
    elif bmi < 30:
        print(f"{word} Overweight")
    elif bmi < 35:
        print(f"{word} Obesity Class I")
    elif bmi < 40:
        print(f"{word} Obesity Class II")
    else:
        print(f"{word} Obesity Class III")
