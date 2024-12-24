spaceCount = 0
vowelCount = 0
digitCount = 0
consonantCount = 0

words = input("Enter your word : ")

for word in words.lower() :
    if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
        vowelCount += 1
    
    elif word == " ":
        spaceCount += 1

    elif "0" <= word <= "9":
        digitCount += 1 
    
    else:
        consonantCount += 1

print(f"Vowel count: \t\t{vowelCount} \nspace count: \t\t{spaceCount} \nConsonant count: \t{consonantCount} \nNumber count: \t\t{digitCount}")
