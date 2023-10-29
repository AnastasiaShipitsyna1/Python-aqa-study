#4. FizzBuzz. Задачка с собеседования
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20) # Вызываем функцию с аргументом 20


#определяет FizzBuzz число
# num = float(input("Enter any number: "))

# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         print ("Number: ", num, "FixxBuzz")
#     elif num % 3 == 0:
#         print("Number: ", num, "Fizz")
#     elif num % 5 == 0:
#         print("Number: ", num, "Buzz")
#     else:
#         print("Add the correct number")

# fizz_buzz(num)