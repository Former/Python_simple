# Copyright 2024 by Alexei Bezborodov <AlexeiBv@narod.ru>

def make_color_text(text, color, bg_color):
    return "\033[3" + str(color) + "m" + "\033[4" + str(bg_color) + "m" + text + "\033[0m"

print(make_color_text("Привет мир!",1,5))
