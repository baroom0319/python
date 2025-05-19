import tkinter
import random
import tkinter.messagebox

result = [
    " 전생에 고양이었을 가능성은 매우 낮습니다.",
    " 보통 사람입니다.",
    " 특별히 이상한 곳은 없습니다.",
    " 꽤 고양이 다운 구석이 있습니다.",
    " 고양이와 비슷한 성격 같습니다.",
    " 고양이와 근접한 성격입닌다.",
    " 전생에 고양이었을지도 모릅니다.",
    " 겉모습은 사람이지만, 속은 고양이일 가능성이 높습니다."
]

#체크버튼 클릭시
def chkBtnClick():
    numCheck = 0
    if cvalue1.get() == True: numCheck += 1
    if cvalue2.get() == True: numCheck += 1
    if cvalue3.get() == True: numCheck += 1
    if cvalue4.get() == True: numCheck += 1
    if cvalue5.get() == True: numCheck += 1
    if cvalue6.get() == True: numCheck += 1
    if cvalue7.get() == True: numCheck += 1
    print(numCheck)

#버튼 클릭시
def btnClick():
    numCheck = 0
    if cvalue1.get() == True: numCheck += 1
    if cvalue2.get() == True: numCheck += 1
    if cvalue3.get() == True: numCheck += 1
    if cvalue4.get() == True: numCheck += 1
    if cvalue5.get() == True: numCheck += 1
    if cvalue6.get() == True: numCheck += 1
    if cvalue7.get() == True: numCheck += 1
    print(numCheck)
    textFilled.delete("1.0",tkinter.END)
    textFilled.insert("1.0"," <진단결과>\n 당신의 고양이 지수는"
                      +str(int(numCheck/7*100))+"%입니다. \n"
                      +result[numCheck])


# 마우스 좌표 값 함수
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse.config(text=str(x)+","+str(y))
  
    labelMouse.place(x=0, y=0)

# 캔버스 만들기
root = tkinter.Tk()
root.title("캔버스 만들기기")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

# 캔버스 내 이미지 생성
bgimg = tkinter.PhotoImage(file="mina.png")
canvas.create_image(400, 300, image=bgimg)


#마우스 좌표 값
root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은고딕", 10))

text = tkinter.Text()
text.place(x=0,y=600, width=800, height=200)


#체크버튼
cvalue1 = tkinter.BooleanVar()
cvalue2 = tkinter.BooleanVar()
cvalue3 = tkinter.BooleanVar()
cvalue4 = tkinter.BooleanVar()
cvalue5 = tkinter.BooleanVar()
cvalue6 = tkinter.BooleanVar()
cvalue7 = tkinter.BooleanVar()


cvalue1.set(False)
cvalue2.set(False)
cvalue3.set(False)
cvalue4.set(False)
cvalue5.set(False)
cvalue6.set(False)
cvalue7.set(False)

cbtn1 = tkinter.Checkbutton(text="높은 곳이 좋다.", variable=cvalue1, command=chkBtnClick,bg="#CFF7EB")
cbtn2 = tkinter.Checkbutton(text="공을 보면 굴리고 싶어진다.", variable=cvalue2, command=chkBtnClick,bg="#CFF7EB")
cbtn3 = tkinter.Checkbutton(text="깜짝 놀라면 털이 곤두선다.", variable=cvalue3, command=chkBtnClick,bg="#CFF7EB")
cbtn4 = tkinter.Checkbutton(text="쥐구머이 마음에 든다.", variable=cvalue4, command=chkBtnClick,bg="#CFF7EB")
cbtn5 = tkinter.Checkbutton(text="개에게 적대감을 느낀다.", variable=cvalue5, command=chkBtnClick,bg="#CFF7EB")
cbtn6 = tkinter.Checkbutton(text="생선 뼈를 발라 먹고 싶다.", variable=cvalue6, command=chkBtnClick,bg="#CFF7EB")
cbtn7 = tkinter.Checkbutton(text="밤, 기운이 난다.", variable=cvalue7, command=chkBtnClick,bg="#CFF7EB")

ygap = 40
cbtn1.place(x=402, y=165+ygap*0)
cbtn2.place(x=402, y=165+ygap*1)
cbtn3.place(x=402, y=165+ygap*2)
cbtn4.place(x=402, y=165+ygap*3)
cbtn5.place(x=402, y=165+ygap*4)
cbtn6.place(x=402, y=165+ygap*5)
cbtn7.place(x=402, y=165+ygap*6)



textFilled = tkinter.Text()
textFilled.place(x=330, y=50, width=420, height=90)

btn = tkinter.Button(text="진단하기",font=("맑은고딕", 24), bg="#CFF7EB", command=btnClick)
btn.place(x=430, y=480, width=150, height=60)



root.mainloop() 

