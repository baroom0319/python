#num1 = 100
#num2 = 200

#print(num1, "+",num2, "=", num1 + num2)
#print(num1, "-",num2, "=", num1 - num2)
#print(num1, "*",num2, "=", num1 * num2)
#print(num1, "%",num2, "=", num1 % num2)

#print("## 택배를 보내기 위한 정보를 입력하세요.##")
#a = input("받는사람: ")
#b = input("주소: ")
#c = input("무게(g): ")

#print("**받는사람 ==>", a)
#print("**주소 ==>", b)
#print("**무게(g) ==>", c)

#strIn = input("원본 문자열 ==> ") #N자리 문자열
#strOut = strIn[3]+strIn[2]+strIn[1]+strIn[0]
#반복문!
#n = len(strIn)
#print(n)
#print("반대 문자열 ==>",strOut)

#age = int(input("나이를 입력 ==> "))
#if age >= 19 :
#    print("즐거운 시간 되세요 ^^")
#else :
#    print("집에 갈 시간이네요!")
#    print("협조 감사합니다.")

#for i in range(1, 5, 2): #1, 3 2번
    #for j in range(2, 4, 1): #2, 3 2번+1 3번
        #print("안녕하세요.")
        #if j%2 == 0:
            #break
        #print("안녕하세요.")
    #print("안녕하세요.")

score = int(input("점수를 입력 ==> "))
if score >= 90 :
    print("A", end='')
elif score >= 80 :
    print("B", end='')
elif score >= 70 :
    print("C", end='')
elif score >= 60 :
    print("D", end='')
else :
    print("F", end='')
print("학점입니다.")

i, hap = 0, 0
for i in range(1001, 2001, 2) :
    hap += i
    print("1000에서 2000까지의 홀수의 합 :", hap)

    