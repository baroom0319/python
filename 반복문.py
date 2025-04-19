i = 0
fact = 1
friends_num = 5
for i in range(1, friends_num+1, 1):
    fact = fact * i
print("A, B, C, D, E 학생들을 순서대로 세우는 경우의 수:", fact)

i = 0
hap = 0
for i in range(1, 11, 1) :
    hap = hap + i
print("1에서 10까지의 합 : ", hap)

i, hap = 0, 0
for i in range(1001, 2001, 2) :
    hap += i
print("1000에서 2000까지의 홀수의 합 :", hap)

i = 0
for i in range(2, 10, 1) :
    for k in range(1, 10, 1) :
        print(i, " X ", k, " = ", i*k)

hap = 0
num1, num2 = 0, 0
while True :
    num1 = int(input("숫자1 ==> "))
    num2 = int(input("숫자2 ==> "))
    hap = num1 + num2
    print(num1, "+", num2, "=", hap)