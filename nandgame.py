def NAND(a, b):
    if a:
        if b:
            return 0
    return 1

print('NAND(1,1)=', NAND(1, 1))

def INV(a):
    return NAND(a, a)

print('INV(1)=', INV(1))

def AND(a,b):
    return INV(NAND(a, b))

def OR(a, b):
    return NAND(INV(a), INV(b))

def XOR(a, b):
    return AND(OR(a, b), NAND(a, b))

def HALF_ADD(a, b):
    return AND(a, b), XOR(a, b)

h,l = HALF_ADD(1,1)
print('HALF_ADD(1,1)=', h, l)

def FULL_ADD(a, b, c):
    h,l = HALF_ADD(a, b)
    h1,l1 = HALF_ADD(l, c)
    return OR(h1, h), l1 

h,l = FULL_ADD(1,1,1)
print('FULL_ADD(1,1)=', h, l)

def MULTI_BIT_ADD(a, b, c):
    h = 0
    result = [0]*len(a)
    for i in range(len(a)):
        h, l = FULL_ADD(a[i], b[i], c)
        result[i] = l
        c = h
    return h, result 

h,r = MULTI_BIT_ADD([1, 0],[1, 1],1)
print('MULTI_BIT_ADD([1, 0],[1, 1],1)=', h, r)
