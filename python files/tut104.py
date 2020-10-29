age_dob = input("Enter your age or year of birth: ")
year = input("Enter any year and know your age in that year: ")

if len(age_dob)<4 & len(year) == 4 :
    age_dob = int(age_dob)
    year = int(year)
    n = 100-age_dob
    hund_year1 = 2020+n
    dob = 2020-age_dob
    pdt1= year-dob
    if age_dob<101:
        print(f"In {hund_year1} CE your age will be 100 year")
    elif age_dob == 100:
        print("You are alrady 100 year old ")
    elif 121>age_dob>100:
        print("you alrady cross 100 year ")
    else:
        print("You are oldest person alive ")

    if pdt1<0:
        print(f"In {year} CE you are not born.")
    else:
        print(f"In {year} CE your age: {pdt1} year")
 
elif len(age_dob) == 4 & len(year) == 4 :
    age_dob = int(age_dob)
    year = int(year)
    hund_year2 = 100+age_dob
    pdt2 = year-age_dob
    if age_dob<1900:
        print("You are oldest person alive ")
    elif 1899<age_dob<1920:
        print("you alrady cross 100 year ")
    elif age_dob == 1920:
        print("You are alrady 100 year old ")
    elif 1920<age_dob<2021:
        print(f"In {hund_year2} CE your age will be 100 year")      
    else :
        print("DOB cant be grater than 2020.")

    if pdt2<0:
        print(f"In {year} CE you are not born.")
    else:
        print(f"In {year} CE your age: {pdt2} year")

else:
    print("Wrong Input!")
