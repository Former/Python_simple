# Copyright 2024 by Alexei Bezborodov <AlexeiBv@narod.ru>

black_ladia = '♜'
black_hource = '♞'
black_elephant = '♝'
black_kind = '♛'
black_ferz = '♚'
black_peshka = '♟'

white_ladia = '♖'
white_hource = '♘'
white_elephant = '♗'
white_kind = '♕'
white_ferz = '♔'
white_peshka = '♙'

line = '+-' * 8 + "+"
print(line)

d = '|'
main_line = d + black_ladia + d + black_hource + d + black_elephant + d + black_kind + d + black_ferz + d + black_elephant + d + black_hource + d + black_ladia + d
print(main_line)
print(line)

peshka_line = (d + black_peshka) * 8 + d
print(peshka_line)
print(line)
