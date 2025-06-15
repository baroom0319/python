# 아래는 요청한 10가지 기능을 포함하여 수정된 코드입니다.

import tkinter
import random
import time
from tkinter import messagebox

# 전역 변수
index = 0
timer = 0
score = 0
hisc = 0
joker_ready = 0
joker_flag = False
joker_used = False
joker_pos = (-1, -1)
difficulty = 0
tsugi = 0
cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
frame_count = 0
last_place_time = 0
place_count = 0

neko = []
check = []
for i in range(12):  # 10x12 공간으로 확장
    neko.append([0]*10)
    check.append([0]*10)

# 하이스코어 불러오기
try:
    with open("hisc.txt", "r") as f:
        hisc = int(f.read())
except:
    hisc = 0

# 마우스 이벤트

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def draw_neko():
    cvs.delete("NEKO")
    for y in range(12):
        for x in range(10):
            if neko[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(12):
        for x in range(10):
            check[y][x] = neko[y][x]
    # 세로 검사
    for y in range(1, 11):
        for x in range(10):
            if check[y][x] > 0:
                if check[y-1][x] in (check[y][x], 8) and check[y+1][x] in (check[y][x], 8):
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7
    # 가로 검사
    for y in range(12):
        for x in range(1, 9):
            if check[y][x] > 0:
                if check[y][x-1] in (check[y][x], 8) and check[y][x+1] in (check[y][x], 8):
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7
    # 대각선 검사
    for y in range(1, 11):
        for x in range(1, 9):
            if check[y][x] > 0:
                if check[y-1][x-1] in (check[y][x], 8) and check[y+1][x+1] in (check[y][x], 8):
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7
                if check[y+1][x-1] in (check[y][x], 8) and check[y-1][x+1] in (check[y][x], 8):
                    neko[y+1][x-1] = 7
                    neko[y][x] = 7
                    neko[y-1][x+1] = 7
    # 2x2 네모 검사
    for y in range(11):
        for x in range(9):
            if check[y][x] > 0:
                c = check[y][x]
                if all(check[yy][xx] in (c, 8) for yy, xx in [(y, x+1), (y+1, x), (y+1, x+1)]):
                    neko[y][x] = 7
                    neko[y][x+1] = 7
                    neko[y+1][x] = 7
                    neko[y+1][x+1] = 7

def sweep_neko():
    num = 0
    for y in range(12):
        for x in range(10):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num += 1
    if num >= 10:
        return num, True
    return num, False

def drop_neko():
    flg = False
    for y in range(10, -1, -1):
        for x in range(10):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():
    for x in range(10):
        if neko[0][x] > 0:
            return True
    return False

def set_neko():
    global tsugi, joker_ready
    if joker_ready >= 5:
        tsugi = 8  # 조커블럭
        joker_ready = 0
        global joker_flag
        joker_flag = True
    else:
        tsugi = random.randint(1, difficulty)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, timer, score, hisc, difficulty, tsugi, frame_count
    global cursor_x, cursor_y, mouse_c, last_place_time, place_count
    global joker_flag, joker_pos, joker_used, joker_ready
    frame_count += 1

    if index == 0:
        draw_txt("야옹야옹", 360, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 552, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 360, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 552, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 360, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 552, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 360, 708, 40, "white", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1:
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x < 552:
                if 384 < mouse_y < 456:
                    difficulty = 4
                elif 528 < mouse_y < 600:
                    difficulty = 5
                elif 672 < mouse_y < 744:
                    difficulty = 6
        if difficulty > 0:
            for y in range(12):
                for x in range(10):
                    neko[y][x] = 0
            score = 0
            tsugi = 0
            place_count = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
    elif index == 2:
        if drop_neko() == False:
            index = 3
        draw_neko()
        if joker_flag and not joker_used:
            joker_pos = (cursor_y, cursor_x)
            joker_used = True
    elif index == 3:
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:
        sc, bonus = sweep_neko()
        score += sc * difficulty * 2
        if bonus:
            score += 10
        if score > hisc:
            hisc = score
        if sc > 0:
            index = 2
        else:
            if not over_neko():
                set_neko()
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()
    elif index == 5:
        if frame_count - last_place_time > 50:
            y, x = cursor_y, cursor_x
            neko[y][x] = tsugi
            place_count += 1
            joker_used = False
            last_place_time = frame_count
            index = 2
        elif 24 <= mouse_x < 24 + 72 * 10 and 24 <= mouse_y < 24 + 72 * 12:
            cursor_x = int((mouse_x - 24) / 72)
            cursor_y = int((mouse_y - 24) / 72)
            if mouse_c == 1:
                mouse_c = 0
                neko[cursor_y][cursor_x] = tsugi
                place_count += 1
                if tsugi != 8:
                    joker_ready += 1
                else:
                    joker_flag = False
                joker_used = False
                last_place_time = frame_count
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:
        timer += 1
        if timer == 1:
            draw_txt("GAME OVER", 360, 348, 60, "red", "OVER")
        if timer == 50:
            with open("hisc.txt", "w") as f:
                f.write(str(hisc))
            cvs.delete("OVER")
            index = 0

    # ESC 키 처리 및 화면 정보
    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 450, 60, 32, "yellow", "INFO")
    draw_txt("TIME " + str(frame_count), 720, 60, 32, "green", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

# ESC 종료 처리

def key_press(event):
    global index, timer, mouse_c
    if event.keysym == "Escape":
        result = tkinter.messagebox.askyesno("게임 종료", "게임을 종료하시겠습니까?")
        if result:
            # 게임 상태 초기화
            cvs.delete("all")  # 캔버스를 완전히 초기화
            for y in range(12):
                for x in range(10):
                    neko[y][x] = 0
                    check[y][x] = 0
            index = 0
            timer = 0
            mouse_c = 0

# 메인 영역
root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<KeyPress>", key_press)
cvs = tkinter.Canvas(root, width=912, height=864)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png"),
    tkinter.PhotoImage(file="춘식.png")
]
cvs.create_image(456, 432, image=bg)
game_main()
root.mainloop()



