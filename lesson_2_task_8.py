#8. Range
#Создайте список [ 18, 14, 10, 6, 2 ] с помощью функции range() и выведите его на экран.
lst =  list(range(18, 1, -4))
print(lst)






#Функция range() в Python представляет собой встроенную функцию, которая создает 
#последовательность чисел в заданном диапазоне. Эта последовательность может использоваться, 
#например, для создания циклов, итерации по элементам и других сценариев.

#Синтаксис функции range() выглядит следующим образом:
#range([start], stop[, step])
# start (необязательный) - начальное значение последовательности. По умолчанию равно 0.
# stop (обязательный) - значение, до которого будет идти последовательность (не включая stop).
# step (необязательный) - шаг, с которым последовательность будет генерироваться. По умолчанию равен 1.
# range() создает объект, который представляет собой последовательность целых чисел от start до stop - 1
# с заданным шагом step.

# my_range = range(1, 10, 2)  # Создает последовательность [1, 3, 5, 7, 9] start =1, stop = 10, step = 2


# for num in range(5): # код выведет числа от 0 до 4
#  print(num)