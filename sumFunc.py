def sumFunc(user):
    print(user+"님. 두 숫자를 입력하세요.")
    num1 = int(input("정정수1 ==> "))
    num2 = int(input("정수2 ==> "))
    hap = num1 + num2
    print("결과 : ", hap)
    return hap

hap = sumFunc("A")
print("결과 : ", hap)
sumFunc("B")
sumFunc("C")