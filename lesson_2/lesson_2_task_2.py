#Високосный год

year = int(input("Enter the year:"))

def is_year_leap(year):
    if (year % 4 == 0 and year %100 !=0) or (year % 400 ==0):
        print("Year:", year, "True")
    else:
        print("Year:", year,"False")

is_year_leap(year)