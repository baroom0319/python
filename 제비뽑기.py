import tkinter
import random

def click_btn():
    label["text"] = random.choice(["대길","중길","소길","흉"])
    label.update()


root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="C:/Users/USER/Downloads/miko.png")
canvas.create_image(400, 300, image=gazou)

label = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg= "white")
label.place(x=360, y=36)
button = tkinter.Button(root, text="제비뽑기", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=360, y=400)

root.mainloop() 
