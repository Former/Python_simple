# -*- coding: utf-8 -*-
# Copyright 2022 by Alexei Bezborodov <AlexeiBv@narod.ru>

width = 3 # ширина
height = 3 # высота

# Разделительная линия
table_line = ""
for i in range(width):
    table_line += "+--"
table_line += "+"

# Таблица
delim = "| "
for y in range(height):
    print(table_line)
    data_line = ""
    for x in range(width):
        data_line += delim + " "
    print(data_line + delim)
print(table_line)
