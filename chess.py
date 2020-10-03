'''
8	♜	♞	♝	♛	♚	♝	♞	♜
7	♟	♟	♟	♟	♟	♟	♟	♟
6	
5	
4	
3	
2	♙	♙	♙	♙	♙	♙	♙	♙
1	♖	♘	♗	♕	♔	♗	♘	♖
    a	b	c	d	e	f	g	h

'''

board = [
'♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', 
' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
'♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖',
]
hor_line = '-----------------'
ver_line_char = '|'

while True:

    # Чистим экран
    for y in range(30):
        print("")

    # Рисуем доску
    cur_x = 0
    cur_y = 0
    print(hor_line)
    for c in board:
        if cur_x == 0:
            print(ver_line_char, sep="", end="")
    
        print(c, sep="", end=ver_line_char)
    
        cur_x += 1
        if cur_x > 7:
            cur_x = 0
            cur_y += 1
            print("")
            print(hor_line)
    
    x1 = int(input("Введите х1:"))
    y1 = int(input("Введите y1:"))
    x2 = int(input("Введите х2:"))
    y2 = int(input("Введите y2:"))

    # Делаем ход
    char1 = board[y1*8 + x1]
    char2 = board[y2*8 + x2]
    if char1 == ' ' or not char2 == ' ':
        print("Ход невозможен")
    else:
        board[y2*8 + x2] = char1
        board[y1*8 + x1] = char2

