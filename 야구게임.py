import random

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = 0
count = 10
random.shuffle(n)

collect = n[0]*100 + n[1]*10 + n[2]




while collect != ans and count > 0:
    s = 0
    b = 0
    o = 0
    ans = int(input("중복되지 않는 3자리 숫자를 입력하세요: "))
    n_100 = ans // 100
    n_10 = ans % 100 // 10
    n_1 = ans % 10

    if n_100 == n[0]:
        s = s + 1
    elif n_100 == n[1] or n_100 == n[2]:
        b = b + 1
    else :
        o = o + 1
    
    if n_10 == n[1]:
        s = s + 1
    elif n_10 == n[0] or n_10 == n[2]:
        b = b + 1
    else :
        o = o + 1
    
    if n_1 == n[2]:
        s = s + 1
    elif n_1 == n[0] or n_1 == n[1]:
        b = b + 1
    else :
        o = o + 1

    count = count - 1
    print("s =", s, "/b =", b, "/o =", o, " >> ", count ,"번 남았습니다.")

if collect == ans:
    print("승리!")
else:
    print("패배... // 정답은 ", collect)