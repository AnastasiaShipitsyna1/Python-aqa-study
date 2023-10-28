#5. Месяц — сезон

# month = int(input("Input number of the month:"))

# month_names = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }


# def month_to_season(month):
#     if 1 <= month <= 12:
#         if month == 12 or month == 1 or month == 2:
#             print ("Winther,", "your month is", month_names[month])
#         elif month == 3 or month == 4 or month == 5:
#             print ("Spring,", "your month is", month_names[month])
#         elif month == 6 or month == 7 or month == 8:
#             print ("Summer,", "your month is", month_names[month])
#         else:
#             print ("Autumm,", "your month is", month_names[month])
#     else: 
#         print("Input a correct number of the month")


# month_to_season(month)



#version#2


month = int(input("Input the month number: "))

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def month_to_season(month):
    if 1 <= month <= 12:
        if month in [12, 1, 2]:
            print("Winter, your month is", month_names[month])
        elif month in [3, 4, 5]:
            print("Spring, your month is", month_names[month])
        elif month in [6, 7, 8]:
            print("Summer, your month is", month_names[month])
        else:
            print("Autumn, your month is", month_names[month])
    else: 
        print("Input a correct month number.")

month_to_season(month)
