# 6. Фильтрация списка
# Heобходимо вывести элементы, которые одновременно:
#     1. меньше 30,
#     2. делятся на 3 без остатка.


lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for n in lst:
    if n < 30 and n % 3 ==0:
        print(n)