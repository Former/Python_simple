# Copyright 2022 by Alexei Bezborodov <AlexeiBv@narod.ru>
maxx = 0
b = 0
for i in range(1, 1001):
    count = 0
    s = i # Начальное значение
    
    print('------------------')
    
    while s != 1:
        if count >= 1000000:
            break
        if s % 2 == 0:
            s = s // 2
        else:
            s = s * 3 + 1
        print(s, bin(s))
    
        count = count + 1
    if count >= maxx:
        maxx = count
        b = i
        
print("Для", b, "будет максимум чисел в последовательности", maxx)
