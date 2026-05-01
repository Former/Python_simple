# Copyright 2025 by Alexei Bezborodov <AlexeiBv@narod.ru>

import random

data = []
for i in range(random.randint(20,200)):
	for j in range(random.randint(1,20)*2):
		data += [i]

data += [random.randint(300,400)]
data += [random.randint(500,600)]

print(data)

xor_all = 0;
for i in range(len(data)):
	xor_all ^= data[i]
print(xor_all)

xor_all_invert = 0;
for i in range(len(data)):
	c = data[i]
	#if i % 2:
	#c = ~c
	xor_all_invert ^= ~c 
print(xor_all_invert)

summ1 = 0;
for i in range(len(data)):
	c = data[i]
	#if i % 2:
	#c = ~c
	summ1 += c 
print(summ1)

summ2 = 0;
for i in range(len(data)):
	c = data[i]
	if i % 2:
		c = ~c
	summ2 += c 
print(summ2)
