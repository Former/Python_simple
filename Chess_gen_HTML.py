# Copyright 2022 by Alexei Bezborodov <AlexeiBv@narod.ru>

data =  "♜♞♝♛♚♝♞♜"\
        "♟♟♟♟♟♟♟♟"\
        "________"\
        "________"\
        "________"\
        "________"\
        "♙♙♙♙♙♙♙♙"\
        "♖♘♗♕♔♗♘♖"

print("<table border=1>")
for i_row in range(8):
    print("<tr>", end="")
    for i_col in range(8):
        color = ""
        if (i_row + i_col + 1)%2 == 0:
            color = " bgcolor=#707070"
        print("<td"+ color + ">" + data[i_row * 8 + i_col] + "</td>", end="")
    print("</tr>")
print("</table>")
