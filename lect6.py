
# 실습 1
# 팩토리아 계산기 : 1부터 N까지의 곱

N= 5
res = 1

for i in range(1, N+1, 1):
    res= res * i
print(res)

# 연습1
# 1000 - 2000 사이에서 홀수의 합을 구하는 프로그램

N= 2000
res = 0
for i in range(1001, N+1, 2):
    res= res + i
print(res)

# 중첩 for문
for i in range(0,3,1):
    for k in range(0,2,1):
        #print("i: ",i," k:",k)
        pass

# 실습 2
# 2단부터 9단까지 구구단을 출력하는 구구단 계산기
for num1 in range(2,10,1): # 단
    for num2 in range(1,10,1): # 곱해지는 수
        print(num1, "X", num2,"=\t", num1*num2)
    print("")


#break 문
res = 0
for i in range(1, 101,1):
    if i % 4 == 0:
        continue
    elif i % 3 == 0:
        continue
    res = res + i
print(res)


import random
count = 0
dice1 = 0
dice2 = 0
dice3 = 0

while True :
    count += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    count += 1
    print(count, "회", dice1,dice2,dice3)
    if (dice1 == dice2)and (dice2 == dice3):
        break

print("3개 주사위는 모두", dice1, "입니다.")
print("같은 숫자가 나오기까지", count, "번 던졌습니다.")