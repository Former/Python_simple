# -*- coding: utf-8 -*-

# Copyright © 2021 Alexei Bezborodov. Contacts: <AlexeiBv+gen_test_python@narod.ru>
# License: Public domain: http://unlicense.org/

from enum import Enum
import random

class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)

class AutoNumber(NoValue):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

class Tags(AutoNumber):
    INIT     = () # Определение
    SUMM     = () # Сумма
    MINUS    = () # Минус
    MULTIPLE = () # Умножение
    DIVIDE   = () # Деление
    DIV_INT  = () # Целочисленное деление
    DIV_REM  = () # Остаток от деления
    AND      = () # И логический оператор
    OR       = () # ИЛИ логический оператор
    NOT      = () # НЕ логический оператор
    EQUAL    = () # равно в условии
    GR_EQUAL = () # >равно в условии
    LE_EQUAL = () # <равно в условии
    GREAT    = () # > в условии
    LESS     = () # < в условии
    IF       = () # Условия
    ELSEIF   = () # Повторное условие
    ELSE     = () # Иначе
    PRINT_VARS = ()
    MAX_TAGS = ()

class TagsSet:
    init = {
        Tags.INIT,
        }
    math = {
        Tags.SUMM,
        Tags.MINUS,
        Tags.MULTIPLE,
        Tags.DIVIDE,
        Tags.DIV_INT,
        Tags.DIV_REM,
        }
    logical = {
        Tags.AND,
        Tags.OR,
        Tags.NOT
        }
    condition = {
        Tags.EQUAL,
        Tags.GR_EQUAL,
        Tags.LE_EQUAL,
        Tags.GREAT,
        Tags.LESS,
        }
    print_vars = {
        Tags.PRINT_VARS,
        }
    all_set = init | math | logical | condition | print_vars


class Property:
    rand_seed = 0
    tags = TagsSet.all_set
    var_prefix = "n"
    range_variables = (1, 3) # Количество используемых переменных (от, до)
    range_operators = (1, 2) # Количество используемых операторов (от, до)
    range_constant = (-10, 10) # Константы (от, до)
    range_math_action = (1, 2) # Количество используемых математических действий на каждом шаге
    range_math_nesting = (0, 3) # Вложенность математических операторов

    range_math_try_nest = 0.5 # Войти во вложенность математических операторов
    range_math_change_to_constant = 0.3 # Заменить на константу


def GetRandValue(range_val):
    return random.randint(range_val[0], range_val[1])

def CheckRandRange(range_val):
    return random.random() < range_val


#random.seed(Property.rand_seed)

class CurTestValues:
    tags = Property.tags

    range_constant = Property.range_constant
    max_vars = GetRandValue(Property.range_variables)
    range_math_action = Property.range_math_action
    range_math_nesting = Property.range_math_nesting

    range_math_try_nest = Property.range_math_try_nest
    range_math_change_to_constant = Property.range_math_change_to_constant
    
    var_list = [Property.var_prefix + str(i + 1) for i in range(max_vars)]
    result_code = ""

cur_test_val = CurTestValues()

def CheckSetInSet(set1, set2):
    if len(set1 & set2) > 0:
        return True
    else:
        return False

def CheckValueInSet(val, set_name):
    set_val = {val}
    return CheckSetInSet(set_val, set_name)

def MakeInit(cur_test_val):
    if CheckValueInSet(Tags.INIT, cur_test_val.tags):
        for val in cur_test_val.var_list:
            cur_test_val.result_code += val + " = " + str(GetRandValue(cur_test_val.range_constant)) + "\n"

def GetMathOper(tag):
    if tag == Tags.SUMM:
        return "+"
    elif tag == Tags.MINUS:
        return "-"
    elif tag == Tags.MULTIPLE:
        return "*"
    elif tag == Tags.DIVIDE:
        return "/"
    elif tag == Tags.DIV_INT:
        return "//"
    elif tag == Tags.DIV_REM:
        return "%"

def GetCurMath(cur_test_val, nest_len):
    cur_var = ["", ""]
    for i in range(2):
        if CheckRandRange(cur_test_val.range_math_change_to_constant):
            cur_var[i] = str(GetRandValue(cur_test_val.range_constant))
        elif CheckRandRange(cur_test_val.range_math_try_nest):
            cur_var[i] = "(" + GetCurMath(cur_test_val, nest_len - 1) + ")"
        else:
            cur_var[i] = random.choice(cur_test_val.var_list)
    
    op = GetMathOper(random.sample(cur_test_val.tags & TagsSet.math, 1)[0])
    
    return cur_var[0] + " " + op + " " + cur_var[1]
        

def MakeMath(cur_test_val):
    cur_var = random.choice(cur_test_val.var_list)
    cur_nest = GetRandValue(cur_test_val.range_math_nesting)
    
    cur_test_val.result_code += cur_var + " = " + GetCurMath(cur_test_val, cur_nest) + "\n"

def MakePrintVars(cur_test_val):
    if CheckValueInSet(Tags.PRINT_VARS, cur_test_val.tags):
        cur_test_val.result_code += "print(" + ",".join(cur_test_val.var_list) + ")"

# Запускаем программу

if CheckSetInSet(TagsSet.init, cur_test_val.tags):
    MakeInit(cur_test_val)

if CheckSetInSet(TagsSet.math, cur_test_val.tags):
    for i in range(GetRandValue(cur_test_val.range_math_action)):
        MakeMath(cur_test_val)

if CheckSetInSet(TagsSet.print_vars, cur_test_val.tags):
    MakePrintVars(cur_test_val)

print(cur_test_val.result_code)


print("Ответ:")
exec(cur_test_val.result_code)


