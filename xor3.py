# Copyright © 2025 Alexei Bezborodov. Contacts: <AlexeiBv+xor3@narod.ru>
# License: Public domain: http://unlicense.org/

def to_base(n, base):
	result = []
	while n != 0:
		result += [n % base] 
		n = n // base
	if result == []:
		result = [0];

	return result

def join_base(b, base):
	result = 0
	#b_rev = b[::-1]
	for i in range(len(b)):
		result += b[i] * (base ** i)
	return result
	
def xor_for_base(n1, n2, base):
	b1 = to_base(n1, base)
	b2 = to_base(n2, base)

	result = [0] * max(len(b1), len(b2))
	for i in range(len(result)):
		c1 = 0
		if i < len(b1):
			c1 = b1[i]
		c2 = 0
		if i < len(b2):
			c2 = b2[i]
		result[i] = (c1 + c2 ) % base

	return join_base(result, base)

def xor_array(a, base):
	result = 0
	for n in a:
		result = xor_for_base(result, n, base)
	return result
	
	
def Test():
	assert to_base(10, 2) == [0, 1, 0, 1]
	assert to_base(10, 10) == [0, 1]
	assert join_base([1,1,1], 2) == 7
	assert join_base([0,1], 10) == 10
	assert xor_for_base(7, 7, 2) == 0
	assert xor_for_base(1, 7, 2) == 6
	assert xor_for_base(3, xor_for_base(3, 3, 3), 3) == 0
	
	# В массиве встрчаются строго по 3 значения одинаковых, кроме одного - которое строго одно, например: 4,5,1,5,1,7,4,1,5,4. Найти его за o[n]/o(1)
	d = [4,5,1,5,1,7,4,1,5,4]
	assert xor_array(d, 3) == 7

	# В массиве встрчаются строго по 2,4,6... значения одинаковых, кроме двух, например: 4,5,4,5,10,7,10,7,1,2,4,4. Найти эти два значения (1,2) за o[n]/o(1)
	d = [4,5,4,5,10,7,10,7,11,12] 
	print(xor_array(d, 2))
	print(xor_array(d * 2, 4))
	print(xor_array(d * 3, 6))
	print(xor_array(d * 4, 8))
	assert xor_array(d * 2, 4) == 17*2, xor_array(d * 2, 4)
    # Пока нет решения

Test()


