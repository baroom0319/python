import tkinter

def btn_click():
    grade1 = int(entryLec1.get())
    grade2 = int(entryLec2.get())
    grade3 = int(entryLec3.get())

    A = 4.5
    A0 = 4.0
    B = 3.5

    avg = (str(grade1 * B) + str(grade2 * A0) + str(grade3 * A)) / str(grade1 + grade2 + grade3)
    
    str1 = ("평균 학점 : ", avg)
    labelRes1 = tkinter.Label(root, text=str1, font=("맑은고딕", 10))
    labelRes1.place(x=150, y=120)

def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse.config(text=str(x)+","+str(y))
  
    labelMouse.place(x=10, y=280)

root = tkinter.Tk()
root.title("cu")
root.geometry("250x200")

root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은고딕", 10))

# 텍스트 위치
label1 = tkinter.Label(root, text="파이썬", font=("맑은고딕", 10))
label2 = tkinter.Label(root, text="모바일", font=("맑은고딕", 10))
label3 = tkinter.Label(root, text="액셀", font=("맑은고딕", 10))
label4 = tkinter.Label(root, text="과목(이수학점)", font=("맑은고딕", 10))
label5 = tkinter.Label(root, text="성적", font=("맑은고딕", 10))

label1.place(x=40, y=60)
label2.place(x=40, y=80)
label3.place(x=40, y=100)
label4.place(x=40, y=20)
label5.place(x=150, y=20)

btn = tkinter.Button(root, text="계산", font=("맑은고딕", 10), command=btn_click)
btn.place(x=40, y=140, width=45, height=20)


entryLec1 =  tkinter.Entry(width=4)
entryLec2 =  tkinter.Entry(width=4)
entryLec3 =  tkinter.Entry(width=4)
entryLec1.place(x=150, y=60)
entryLec2.place(x=150, y=80)
entryLec3.place(x=150, y=100)

entryLec1.insert(0,"3.0")
entryLec2.insert(0,"3.0")
entryLec3.insert(0,"3.0")




root.mainloop()
