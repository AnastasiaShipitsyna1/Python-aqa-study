name = "Boy"
pfrase1 = "Hi"
print(pfrase1 +", " + name + "!")

weekdays=[
    "Monday",    #0- index
    "Tuesday",   #1
    "Wednesday", #2
    "Thursday",  #3
    "Friday",    #4
    "Saturday",  #5
    "Sunday"]    #6
totalDays = len(weekdays) #функция  len считает количество элементов в списке
print ("total days in a week:" + " " +str(totalDays))  #  указать что totalDay это строка (стринговое значение)


day1 = weekdays[0]
day2 = weekdays[1]
day3 = weekdays[2]
day4 = weekdays[3]
day5 = weekdays[4]
day6 = weekdays[5]
day7 = weekdays[6]

day_str = ", ".join(weekdays)
print(day_str)


#numbers = [10, 20, 30, 40, 50, 60]
#index     0   1   2   3   4   5
#index    -6   -5 -4  -3   -2  -1  считает с конца


#print(numbers[0])
#print(weekdays [6])

#print(numbers[-1])
#print(numbers[-2])
#print(numbers[-3])
#print(numbers[3])
#print(numbers[-6])
#print(numbers[0])

def sumNumber(a, b): #объявление функции
    result= a + b
    return result
#sumNumber(500, 6) #вызов функции

result = sumNumber(500, 6) 
print(result)

def tryMore(f,m):
    print(f+m)

tryMore(100, 50)

def greet(name):
    print("Hello, " + name)

greet("Bossy!")
greet("Lucky!")
greet("Kibella!")

def calculate(num_1, num_2):
    print("Number 1 =", num_1)
    print("Number 2 =", num_2)
    print("addition")
    print("Total =", num_2 + num_1)

calculate(9, 4)
calculate(10,5)

def calc1(n1, n2):
    print("Num 1 =", n1)
    print("Num 2= ", n2)
    print("multiplication")
    result = n1*n2
    print("Total=", result)
    return result

x=calc1(5,6)
print(x)

def funA():
    print("Start to do A")
    funB()
    print("Finish to do A")

def funB():
    print("Start to do B")
    funC()
    print("Finish to do B")

def funC():
    print("Start to do C")
    funD()
    print("Finish to do C")

def funD():
    print("Start to do D")
    print("Finish to do D")

funA()