total = 0
count = 0

while True:
    check = input("Enter score (or 'q' to quit) : ")

    if check == 'q':    
        break
    
    total += int(check)
    count += 1

print(f"\nResult : \nTotal Scores Entered : {count} \nSum of Scores : {total:,.2f} \nAverage Score : {total / count:,.2f}")
    