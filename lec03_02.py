import tkinter

def btn_click():
    total = 0

    total -= (500 * int(entry2.get() or 0))
    total -= (900 * int(entry4.get() or 0))
    total -= (800 * int(entry6.get() or 0))
    total -= (3500 * int(entry8.get() or 0))
    total -= (700 * int(entry10.get() or 0))
    total -= (1000 * int(entry12.get() or 0))

    total += (1800 * int(entry1.get() or 0))
    total += (1400 * int(entry3.get() or 0))
    total += (1800 * int(entry5.get() or 0))
    total += (4000 * int(entry7.get() or 0))
    total += (1500 * int(entry9.get() or 0))
    total += (2000 * int(entry11.get() or 0))

    str1 = ("오늘 총 매출액은 "+str(total)+"원입니다")
    labelRes1 = tkinter.Label(root, text=str1, font=("맑은고딕", 10))
    labelRes1.place(x=180, y=420)

root = tkinter.Tk()
root.title("cu")
root.geometry("1000x500")

label1 = tkinter.Label(root, text="판매 수량", font=("맑은고딕", 12))
label2 = tkinter.Label(root, text="구매 수량", font=("맑은고딕", 12))

label1.place(x=40, y=150)
label2.place(x=40, y=250)

btn = tkinter.Button(root, text="계산", font=("맑은고딕", 10), command=btn_click)
btn.place(x=180, y=350, width=700, height=48)

label1 = tkinter.Label(root, text="캔 커피", font=("맑은고딕", 10))
label2 = tkinter.Label(root, text="삼각김밥", font=("맑은고딕", 10))
label3 = tkinter.Label(root, text="바나나 우유", font=("맑은고딕", 10))
label4 = tkinter.Label(root, text="도시락", font=("맑은고딕", 10))
label5 = tkinter.Label(root, text="콜라", font=("맑은고딕", 10))
label6 = tkinter.Label(root, text="새우깡", font=("맑은고딕", 10))

label1.place(x=200, y=70)
label2.place(x=320, y=70)
label3.place(x=440, y=70)
label4.place(x=560, y=70)
label5.place(x=680, y=70)
label6.place(x=800, y=70)

entry1 =  tkinter.Entry(width=8)
entry2 =  tkinter.Entry(width=8)
entry1.place(x=200, y=150)
entry2.place(x=200, y=250)

entry3 =  tkinter.Entry(width=8)
entry4 =  tkinter.Entry(width=8)
entry3.place(x=320, y=150)
entry4.place(x=320, y=250)

entry5 =  tkinter.Entry(width=8)
entry6 =  tkinter.Entry(width=8)
entry5.place(x=440, y=150)
entry6.place(x=440, y=250)

entry7 =  tkinter.Entry(width=8)
entry8 =  tkinter.Entry(width=8)
entry7.place(x=560, y=150)
entry8.place(x=560, y=250)

entry9 =  tkinter.Entry(width=8)
entry10 =  tkinter.Entry(width=8)
entry9.place(x=680, y=150)
entry10.place(x=680, y=250)

entry11 =  tkinter.Entry(width=8)
entry12 =  tkinter.Entry(width=8)
entry11.place(x=800, y=150)
entry12.place(x=800, y=250)



root.mainloop()