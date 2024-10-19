# Copyright © 2024 Alexei Bezborodov. Contacts: <AlexeiBv+CONFP_py@narod.ru>
# License: Public domain: http://unlicense.org/

# CONFP Конфиг для настроек в одну функцию (Config ONe Function Parse)
# Позволяет парсить конфигурационный файлы любой сложности. Реализуется в одну функцию

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
        cur_value = result.get(param_name_trim)
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

def CONFP_GetValue(a_ParseResult, a_Key, a_DefaultValue):
    val = a_ParseResult.get(a_Key)
    if not val:
        return a_DefaultValue
    return val

def CONFP_GetIntValue(a_ParseResult, a_Key, a_DefaultIntValue):
    val = a_ParseResult.get(a_Key)
    if not val:
        return a_DefaultIntValue
    return int(val)

def CONFP_GetFloatValue(a_ParseResult, a_Key, a_DefaultFloatValue):
    val = a_ParseResult.get(a_Key)
    if not val:
        return a_DefaultFloatValue
    return float(val)

def CONFP_GetArrayValue(a_ParseResult, a_Key, a_DefaultArrayValue):
    val = CONFP_GetValue(a_ParseResult, a_Key, a_DefaultArrayValue)
    if type(val) == str:
        return [val]
    return val

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
    conf5 = "val={1}"
    conf6 = "val={1};"
    conf7 = conf6*5
    conf8 = """ val1=1
    val2=2
    val3={Hello}
    """
    conf9 = """ val1 = 1
    val2 = 2
    val3 = {Hello}
    """
    conf10 = """val={
    1
    }"""
    conf11 = """val={
    1
    };"""
    conf12 = conf11*5
    conf13 = """val={
    {1}
    }"""
    conf14 = """val={
    {1}
    };"""
    conf15 = conf14*5
    assert {"val":"1"} == CONFP_Parse(conf0)
    assert {"val":"1"} == CONFP_Parse(conf1)
    assert {"val":["1"]*5} == CONFP_Parse(conf2)
    assert {"val1":"1", "val2":"2", "val3":"Hello"} == CONFP_Parse(conf3)
    assert {"val1":"1", "val2":"2", "val3":"Hello"} == CONFP_Parse(conf4)
    assert {"val":"1"} == CONFP_Parse(conf5)
    assert {"val":"1"} == CONFP_Parse(conf6)
    assert {"val":["1"]*5} == CONFP_Parse(conf7)
    assert {"val1":"1", "val2":"2", "val3":"Hello"} == CONFP_Parse(conf8)
    assert {"val1":"1", "val2":"2", "val3":"Hello"} == CONFP_Parse(conf9)
    assert {"val":"1"} == CONFP_Parse(conf10)
    assert {"val":"1"} == CONFP_Parse(conf11)
    assert {"val":["1"]*5} == CONFP_Parse(conf12)
    assert {"val":"{1}"} == CONFP_Parse(conf13)
    assert {"val":"{1}"} == CONFP_Parse(conf14)
    assert ["{1}"] == CONFP_GetArrayValue(CONFP_Parse(conf14), "val", [])
    assert [] == CONFP_GetArrayValue(CONFP_Parse(conf14), "val1", [])

    assert {"val":["{1}"]*5} == CONFP_Parse(conf15)
    assert ["{1}"]*5 == CONFP_GetArrayValue(CONFP_Parse(conf15), "val", [])


    conf16 = """
    ver=0.1.0
    data="test"
    complex1={
        name = test1;
        complex2 = {
            name = test2
        }
        complex2 = {
            name = test3;
        }
    }
    """
    assert "0.1.0" == CONFP_Parse(conf16).get("ver")
    assert '"test"' == CONFP_Parse(conf16).get("data")
    assert "test1" == CONFP_Parse(CONFP_Parse(conf16).get("complex1")).get("name")
    assert "test2" == CONFP_Parse(CONFP_Parse(CONFP_Parse(conf16).get("complex1")).get("complex2")[0]).get("name")
    assert "test3" == CONFP_Parse(CONFP_Parse(CONFP_Parse(conf16).get("complex1")).get("complex2")[1]).get("name")

    conf17 = """
    ver=0.1.0
    int1=-50
    int2=123
    int3 = 0
    float1=-5.0
    float2=12.3
    float3 = .0
    complex1={
        int1=-50
        float1=-5.0
    }
    complex1={
        int1=-150
        float1 = .0
    }
    """
    parse17 = CONFP_Parse(conf17)
    assert "0.1.0" == CONFP_GetValue(parse17, "ver", "")
    assert 10 == CONFP_GetIntValue(parse17, "int", 10)
    assert -50 == CONFP_GetIntValue(parse17, "int1", 0)
    assert 123 == CONFP_GetIntValue(parse17, "int2", 0)
    assert 0 == CONFP_GetIntValue(parse17, "int3", 10)
    assert 10.0 == CONFP_GetFloatValue(parse17, "float", 10.0)
    assert -5.0 == CONFP_GetFloatValue(parse17, "float1", 0.0)
    assert 12.3 == CONFP_GetFloatValue(parse17, "float2", 0.0)
    assert 0.0 == CONFP_GetFloatValue(parse17, "float3", 10.0)
    parse17_complex = CONFP_GetValue(parse17, "complex1", [])
    parse17_0 = CONFP_Parse(parse17_complex[0])
    parse17_1 = CONFP_Parse(parse17_complex[1])
    assert -50 == CONFP_GetIntValue(parse17_0, "int1", 10)
    assert -5.0 == CONFP_GetFloatValue(parse17_0, "float1", 10)
    assert -150 == CONFP_GetIntValue(parse17_1, "int1", 10)
    assert 0.0 == CONFP_GetFloatValue(parse17_1, "float1", 10)

Test()

