
#рисуем мышку

from turtle import *

# Функция для рисования круга
def draw_circle(color, radius, x, y):
    penup()
    fillcolor(color)
    goto(x, y)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()

# Функция для рисования прямоугольника
def draw_rectangle(color, width, height, x, y):
    penup()
    fillcolor(color)
    goto(x, y)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

# Настроим окно и скорость черепахи
screen = Screen()
screen.setup(800, 600)
speed(2)

# Рисуем тело мышки
draw_circle("gray", 40, 0, -50)

# Рисуем голову
draw_circle("gray", 25, 0, 30)

# Рисуем левое ухо
draw_circle("pink", 20, -25, 60)

# Рисуем правое ухо
draw_circle("pink", 20, 25, 60)

# Рисуем левый глаз
draw_circle("white", 8, -12, 45)
draw_circle("black", 4, -8, 50)

# Рисуем правый глаз
draw_circle("white", 8, 12, 45)
draw_circle("black", 4, 16, 50)

# Рисуем нос
draw_circle("pink", 4, 0, 40)

# Рисуем рот
penup()
goto(5, 38)
pendown()
setheading(270)
circle(5, 180)

# Рисуем хвост
penup()
goto(40, -30)
pendown()
setheading(0)
circle(40, 90)

hideturtle()

# Завершение программы по клику
exitonclick()


# from turtle import * #Эта строка импортирует все функции и классы из модуля turtle, 
#                      #что позволяет использовать его методы без указания префикса turtle.

# my_turtle = Turtle()
# my_turtle.speed(0) #Устанавливает максимальную скорость для черепахи. Значение 0 означает максимальную скорость, и черепаха будет рисовать мгновенно
# my_turtle.screen.setup(1200, 800) #Устанавливает размер экрана для черепахи, чтобы создать окно размером 1200x800 пикселей.

# # Нарисовать квадрат  Это функция, которая рисует квадрат. Внутри функции есть цикл for, который поворачивает черепаху на 90 градусов и передвигает ее вперед на 100 единиц, создавая стороны квадрата.
# # def draw_rect(t):
# #     for x in range(0, 4):
# #         t.right(90)
# #         t.forward(100)

# def draw_circle(t): #круг
#     t.circle(100)  # 100 - это радиус круга


# # Рисует квадраты в цикле. Этот цикл поворачивает черепаху на 1 градус вправо и вызывает draw_rect для каждого угла. Это создает анимацию, в результате которой черепаха рисует 360 квадратов, вращаясь вокруг точки.
# # for x in range(0, 360):
# #     draw_rect(my_turtle)
# #     my_turtle.right(1)

# for x in range(0, 360): #смещение круга
#     draw_circle(my_turtle)
#     my_turtle.right(1)


# # Необходимо, чтобы окно не закрывалось само, а только по клику
# my_turtle.screen.exitonclick() #После завершения анимации окно не закроется само, а будет закрыто только после клика мышкой.
# my_turtle.screen.mainloop() #Эта строка выполняет главный цикл событий для окна, чтобы оно оставалось открытым, пока не будет закрыто пользователем.
