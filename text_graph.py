import math

max_x = 64
max_y = 12

mid_x = max_x / 2
mid_y = max_y / 2

for y in range(max_y):
    print("")    
    for x in range(max_x):
        cur_x = x - mid_x
        cur_y = -(y - mid_y)
        function = 5 * math.sin(cur_x / 10)
        
        cur_char = " "
        if cur_y == function // 1:
            cur_char = "*"
        elif y == mid_y:
            cur_char = "-"
        elif x == mid_x:
            cur_char = "|"

        print(cur_char, sep="",end="")