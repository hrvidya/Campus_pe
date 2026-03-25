from datetime import datetime #import datetime to taker currentyear
#here we can do foe edge case in case of leap year,but they asked for 365 approx
try:
    birth_year = int(input("enter your birth year: "))
    current_year = datetime.now().year
    #calculate age
    age=current_year-birth_year
    months=age*12
    days=age*365          
    hours=days*24
    minutes=hours*60
    years_to_100=100-age

    print("\n=== AGE DETAILS ===")
    print("Current Age:", age, "years")
    print("Age in months:", months)
    print("Age in days (approx):", days)
    print("Age in hours:", hours)
    print("Age in minutes:", minutes)

    if years_to_100 > 0:
        print("Years left to reach 100:", years_to_100)
    else:
        print("You are already 100+ years old!")

except ValueError:
    print("Please enter a valid year.")