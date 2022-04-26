# Copyright 2022 by Alexei Bezborodov <AlexeiBv@narod.ru>

# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. 
# Пример входного списка "1 2 56 7" 
#              На выходе "56 2 1 7" 

def swap_min_max(l):
    if len(l) < 2: 
        pass
    min_element_index = 0
    max_element_index = 0
    min_element = l[min_element_index]
    max_element = l[max_element_index]
    for i, cur_element in enumerate(l[1:], 1):
        if max_element < cur_element:
            max_element = cur_element
            max_element_index = i
        if min_element > cur_element:
            min_element = cur_element
            min_element_index = i
    
    l[min_element_index] = max_element
    l[max_element_index] = min_element

l = [int(s) for s in input().split(" ")]

swap_min_max(l)

result = [str(i) for i in l]
print(" ".join(result))
