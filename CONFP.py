# Copyright © 2024 Alexei Bezborodov. Contacts: <AlexeiBv+CONFP_py@narod.ru>
# License: Public domain: http://unlicense.org/

# CONFP Конфиг для настроек в одну функцию (Config ONe Function Parse)

def CONFP_Parse(a_StrToParse):

    pc_guard_char = ['\\']
    pc_break_name = ['=', ':']
    pc_break_value = ['\n', ';']
    pc_start_complex_value = ['{']
    pc_stop_complex_value = ['}']
    
    pt_param_name = 0
    pt_param_value = 1
    pt_complex_value = 2

    result = {}
    def add_to_result(result, param_name, param_value):
        param_name_trim = param_name.strip()
        param_value_trim = param_value.strip()
        if len(param_name_trim) == 0 and len(param_value_trim) == 0:
            return
        cur_value = result.get(param_name)
        if cur_value:
            if type(cur_value) == str:
                cur_value = [cur_value]
            cur_value += [param_value_trim]
        else:
            cur_value = param_value_trim
        result.update({param_name_trim: cur_value})
    parse_type = pt_param_name
    cur_index = 0
    param_name = ""
    param_value = ""
    last_char = ''
    level_index = 0
    while (cur_index < len(a_StrToParse)):
        cur_char = a_StrToParse[cur_index]
        if parse_type == pt_param_name:
            if not last_char in pc_guard_char and cur_char in pc_break_name:
                parse_type = pt_param_value
            else:
                param_name += cur_char
        elif parse_type == pt_param_value:
            if not last_char in pc_guard_char and cur_char in pc_break_value:
                add_to_result(result, param_name, param_value)
                param_name = ""
                param_value = ""
                parse_type = pt_param_name
            elif not last_char in pc_guard_char and cur_char in pc_start_complex_value:
                parse_type = pt_complex_value
            else:
                param_value += cur_char
        elif parse_type == pt_complex_value:
            if not last_char in pc_guard_char and cur_char in pc_stop_complex_value:
                if level_index == 0:
                    parse_type = pt_param_value
                else:
                    level_index -= 1
                    param_value += cur_char
            elif not last_char in pc_guard_char and cur_char in pc_start_complex_value:
                level_index += 1
                param_value += cur_char
            else:
                param_value += cur_char
        last_char = cur_char
        cur_index += 1

    if len(param_name) != 0 or len(param_value) != 0:
        add_to_result(result, param_name, param_value)

    return result

def Test():
    conf0 = "val=1"
    conf1 = "val=1;"
    conf2 = conf1*5
    conf3 = """ val1=1
    val2=2
    val3=Hello
    """
    conf4 = """ val1 = 1
    val2 = 2
    val3 = Hello
    """
    assert {"val":"1"} == CONFP_Parse(conf0)
    assert {"val":"1"} == CONFP_Parse(conf1)
    assert {"val":["1"]*5} == CONFP_Parse(conf2)
    assert {"val1":"1", "val2":"2", "val3":"Hello"} == CONFP_Parse(conf3), CONFP_Parse(conf3)
    assert {"val1":"1", "val2":"2", "val3":"Hello"} == CONFP_Parse(conf4)

Test()
