import tkinter
import random

# 버튼 클릭 시의 함수
def click_btn():
    label["text"] = random.choice(["대길","중길","소길","흉"])
    label.update()

# 캔버스 만들기
root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

# 캔버스 내 이미지 생성
bgimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=bgimg)

# 텍스트 위치
label = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg= "white")
label.place(x=360, y=36)

#버튼 위치
button = tkinter.Button(root, text="제비뽑기", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=360, y=400)

root.mainloop() 
