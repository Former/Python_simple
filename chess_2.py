# -*- coding: utf-8 -*-

width = 3 # ширина
height = 3 # высота

# Данные 
data = [" " for i in range(height * width)]

# Получаем элемент с координатами x, y из данных
def GetElement(x, y):
    return data[y * width + x]

# Печатаем линию для таблицы
def PrintLine(width):
    for i in range(width):
        print("+--", end = "")
    print("+")

# draw - Функция рисования поля для игры
def draw(data):
    mini = "| "
    for y in range(height):
        PrintLine(width)
        for x in range(width):
            print(mini + GetElement(x, y), end = "")
        print(mini)
    PrintLine(width)

while True:
    x = int(input("Введите Х:"))
    y = int(input("Введите У:"))
    
    if x < 0 or x > 2 or y < 0 or y > 2 or GetElement(x, y) != " ":
        print("Так ходить нельзя")
    else:
        data[width * y + x] = "Х"
 
    draw(data)
