#3. Площадь квадрата
param = float(input("Please enter the side size of the square: "))

def square(param):
    area = param * param
    rounded_area = round(area)  # округление
    print("Area of the square =", rounded_area)

square(param)
