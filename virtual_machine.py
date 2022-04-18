# Copyright 2022 by Alexei Bezborodov <AlexeiBv@narod.ru>

# reg[0] = reg[0] * 0
mem1 = (2 << 28) | (2 << 24) | (0 << 20) | (0 << 16) | (0xF << 12) | (0)
# reg_prog_index = reg[0]
mem2 = (1 << 28)

mem = [mem1, mem2] + [0] * 100;
reg_prog_index = 0 # IP
reg = [10] * 16 # reg[0], reg[0]

def Noop():
    return

def ExecuteOneCommand():
    global mem
    global reg_prog_index
    global reg
    
    cur_instuction = mem[reg_prog_index]
    
    # OpType  Math  reg1 reg2 reg3    number
    # 0000  0000  0100 0000 1111  0010 0000 0000
    # (0xF << 20)=1111 0000 0000  0000 0000 0000

    # 0000  0000  0100 0000 0000  0000 0000 0000
    # 0000  0000                            1111
    
    #0xF = 1111
    
    # reg1 = reg2 Math number

    reg1_number = (cur_instuction & (0xF << 20)) >> 20
    reg2_number = (cur_instuction & (0xF << 16)) >> 16
    reg3_number = (cur_instuction & (0xF << 12)) >> 12
    op_math = (cur_instuction & (0xF << 24)) >> 24
    op_type = (cur_instuction & (0xF << 28)) >> 28
    number = cur_instuction & (0xFFF)

    if op_type == 0:
        Noop()
    elif op_type == 1:
        reg_prog_index = reg[0]
    elif op_type == 2:
        if op_math == 0:
            if reg3_number == 15:
                reg[reg1_number] = reg[reg2_number] + number
            else:
                reg[reg1_number] = reg[reg2_number] + reg[reg3_number]
        elif op_math == 1:
            if reg3_number == 15:
                reg[reg1_number] = reg[reg2_number] - number
            else:
                reg[reg1_number] = reg[reg2_number] - reg[reg3_number]
        elif op_math == 2:
            if reg3_number == 15:
                reg[reg1_number] = reg[reg2_number] * number
            else:
                reg[reg1_number] = reg[reg2_number] * reg[reg3_number]
        elif op_math == 3:
            if reg3_number == 15:
                reg[reg1_number] = reg[reg2_number] / number
            else:
                reg[reg1_number] = reg[reg2_number] / reg[reg3_number]
    elif op_type == 3:
        mem[reg[reg1_number]] = reg[reg2_number]
    elif op_type == 4:
        reg[reg1_number] = mem[reg[reg2_number]]

    reg_prog_index += 1
    return

for i in range(100):
    #print("mem", mem)
    print("reg_prog_index =", reg_prog_index)
    print("reg =", reg)
    ExecuteOneCommand()
    
    
''' 
DEBUG
    print("cur_instuction=", cur_instuction)

    print("reg1_number=", reg1_number)
    print("reg2_number=", reg2_number)
    print("reg3_number=", reg3_number)
    print("op_math", op_math)
    print("op_type", op_type)
    print("number", number)
'''
