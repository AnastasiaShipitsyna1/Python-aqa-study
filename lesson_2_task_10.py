# 10. Банковское приложение*
# 2. Дано**:** пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых 
#(каждый год размер его вклада увеличивается на 10%, эти деньги прибавляются к сумме вклада, 
#и на них в следующем году тоже будут проценты).
# 3. Задача: написать функцию bank, принимающую аргументы X и Y и возвращающую сумму, 
#которая будет на счету пользователя спустя Y лет.

X = float(input("Input the amount of the deposit, rub: ")) #ammount
Y = int(input("Enter the number of years for which you want to lock the deposit: ")) #years
interest_rate = 0.10

def bank(X, Y):
    for _ in range(Y):
        X += X * interest_rate
    return X

result = bank(X, Y)
print(f"The amount on the account after {Y} years will be: {result:.2f} rubles")
