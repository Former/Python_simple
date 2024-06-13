# Copyright 2024 by Alexei Bezborodov <AlexeiBv@narod.ru>
# Общественное достояние (public domain)
# Простые шахматы, без проверок на правильность хода

wigth = 8 # Ширина доски
heigth = 8 # Высота доски

board_chars = "abcdefgh" # буквы на доске
board = ['♖','♘','♗','♕','♔','♗','♘','♖'] + wigth * ['♙'] + (heigth - 4) * wigth * [' '] + wigth * ['♟'] + ['♜','♞','♝','♛','♚','♝','♞','♜'] # фигуры на доске

horisontal_line = ' ' + (2 * wigth + 1) * '-' # горизонтальная линия доски
vertical_line_char = '|' # вертикальный символ клетки
str_bad_command = "Ход невозможен"

# Всего 30 ходов
for i in range(30):
    # Выводим доску
    print(horisontal_line)
    for row_number in range(heigth):
        line = str(row_number + 1) # Номера строк
        for stolb_number in range(wigth):
            line += vertical_line_char + board[row_number * wigth + stolb_number] # фигуры
        print(line + vertical_line_char)
        print(horisontal_line)

    # Буквы для столбцов
    line = ' '
    for stolb_number in range(wigth):
        line += ' ' + board_chars[stolb_number]
    print(line)

    # Спрашиваем ход у пользователя
    user_command = input("Введите ход (например e2e4):")

    if len(user_command) != 4:
        print(str_bad_command)
        continue;

    # Вычисляем координаты
    x1 = board_chars.find(user_command[0])
    y1 = int(user_command[1]) - 1
    x2 = board_chars.find(user_command[2])
    y2 = int(user_command[3]) - 1
    if x1 == -1 or x2 == -1 or y1 < 0 or y1 >= heigth or y2 < 0 or y2 >= heigth:
        print(str_bad_command)
        continue;
    
    # Делаем ход
    tmp = board[y2 * wigth + x2]
    board[y2 * wigth + x2] = board[y1 * wigth + x1]
    board[y1 * wigth + x1] = tmp

