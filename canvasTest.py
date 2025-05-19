import tkinter

root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

root = tkinter.Tk()
root.title("캔버스 만들기")
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")

bgimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=bgimg)

canvas.pack()
root.mainloop()
