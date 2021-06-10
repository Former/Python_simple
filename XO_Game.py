import random
SPACE = " "
X = "X"
O = "O"

# True/False
# Проверка на то что всё поле заполнено, при этом возвращается True. Иначе False
def AllDataFill(w, h, data): 
    result = True
    for i in range(w * h):
        if data[i] == SPACE:
            result = False    
            break
    return result

# Один ход компьютерного игрока, который случайно ставит либо крестики либо нолики (put_element)
def ComputerAI_PutElement(w, h, data, put_element):
    while True:                                                                                 
        r = int(random.random() * w * h) # random.randint(0, w * h - 1)
        if data[r] == SPACE:
            data[r] = put_element
            break
    return data  

# Отрисовка поля
def Draw(w, h, data):
    line = '+--'
    for s in range(h):
        print(line * w + '+')
        print('| ' + '| '.join(data[s*w:(s+1)*w]) + '|')

    print(line * w + '+')

# True/False
# Выиграл ли Х или О
def CheckWin(w, h, data, check_element):
    def GetElement(data, x, y, w, h):
        return data[w*y + x]
    
    # минимально возможное значение
    l = min(w, h)    
    
    # Все значения     
    all_seq_fill = [i for i in range(l)]  # Например, для l = 3: [0, 1, 2]

    all_seq_fill_by_l = [i // l for i in range(l*l)]  # Например, для l = 3: [0, 0, 0, 1, 1, 1, 2, 2, 2]
    
    #          строки              столбцы            1 диагональ     2 диагональ
    check_x = all_seq_fill * l  + all_seq_fill_by_l + all_seq_fill + all_seq_fill[::-1]
    check_y = all_seq_fill_by_l + all_seq_fill * l  + all_seq_fill + all_seq_fill

    for i in range(0, len(check_x), l):
        check_line = [GetElement(data, check_x[i+k], check_y[i+k], w, h) for k in range(l)] 
        result = True
        for element in check_line:
            if element != check_element:
                result = False
        if result:
            break
    
    return result

def Test():
    print("Test CheckWin")
    for element in X, O:
        print(1, CheckWin(3, 3, [element, SPACE, SPACE, element, SPACE, SPACE, element, SPACE, SPACE], element), True)
        print(2, CheckWin(3, 3, [SPACE, SPACE, element, SPACE, SPACE, element, SPACE, SPACE, element], element), True)
        print(3, CheckWin(3, 3, [SPACE , SPACE, element,  SPACE, SPACE, SPACE, element, SPACE, SPACE], element), False)
        print(4, CheckWin(2, 2, [element, SPACE, SPACE, element], element), True)
        print(5, CheckWin(2, 2, [SPACE, element, SPACE, element], element), True)
        print(6, CheckWin(3, 3, [element, element, element, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE], element), True) 
        print(7, CheckWin(3, 3, [SPACE, SPACE, SPACE, element, element, element, SPACE, SPACE, SPACE], element), True)
        print(8, CheckWin(3, 3, [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, element, element, element], element), True)
        print(9, CheckWin(3, 3, [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE], element), False)
        print(10, CheckWin(3, 3, [element, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE], element), False)
        print(11, CheckWin(3, 3, [element, element, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE], element), False)
        print(12, CheckWin(3, 3, [element, SPACE, SPACE, SPACE, SPACE, element, SPACE, SPACE, SPACE], element), False)
        print(13, CheckWin(3, 3, [element, element, SPACE, SPACE, SPACE, SPACE, element, SPACE, SPACE], element), False)
        print(14, CheckWin(3, 3, [element, SPACE, SPACE, SPACE, element, SPACE, SPACE, SPACE, element], element), True)
        print(15, CheckWin(3, 3, [SPACE, SPACE, element, SPACE, element, SPACE, element, SPACE, SPACE], element), True)

    print("Test CheckForWin")


# Game start

#Test()
#exit()

w = 3
h = 3
data = [SPACE] * w * h

while True:
    Draw(w, h, data)

    x = int(input("Введите координату (x):"))
    y = int(input("Введите координату (y):"))

    if x >= 1 and x <= w and y >= 1 and y <= h and data[w * (y - 1) + (x - 1)] == SPACE:
        data[w * (y - 1) + (x - 1)] = X
    else:
        print("Так ходить нельзя")
        continue
    
    if CheckWin(w, h, data, X) == True:
        print("Пользователь победил")
        Draw(w, h, data)
        break

    if AllDataFill(w, h, data) == True:
        print("Ничья")
        Draw(w, h, data)
        break

    ComputerAI_PutElement(w, h, data, O)

    if CheckWin(w, h, data, O) == True:
        print("Компьютер победил")
        Draw(w, h, data)
        break


