def calc(v1, v2, op):
    res = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    return res

value = 0
v1 = 0
v2 = 0
op = ""

op = input("계산 입력 (+, -, *, /)")
v1 = int(input("첫번째 숫자 입력 : "))
v2 = int(input("두번째 숫자 입력 : "))
value = calc(v1, v2 ,op)
print("##계산기 :", v1,op,v2,"=",value)