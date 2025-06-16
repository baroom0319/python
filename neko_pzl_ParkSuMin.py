import tkinter
import tkinter.messagebox
import random

# 전역 변수 영역
index = 0
timer = 0
score = 0
hisc = 0
difficulty = 0
tsugi = 0
timerCount = 0
timer_active = False
timer_id = None
no_input_time = 0 
game_loop_running = False
joker_count = 0         # 수동 배치 카운트
joker_pending = []      # [(y, x), ...] 1턴 후 변환될 조커 위치 저장

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

neko = []
check = []
destroyed = []
for i in range(12):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0, 0 ,0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    destroyed.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def load_hisc():
    global hisc
    try:
        with open("hisc.txt", "r") as f:
            hisc = int(f.read())
    except:
        hisc = 0

def save_hisc():
    global hisc
    with open("hisc.txt", "w") as f:
        f.write(str(hisc))


# 타이머 함수 추가
def countUp():
    global tmr
    if timer_active:  # 게임 진행 중일 때만 카운트 #타이머 활성 상태일 때만 증가
        tmr += 1
        cvs.delete("TIMER")
        draw_txt(f"TIME {tmr}s", 700, 60, 32, "green", "TIMER")
        root.after(1000, countUp)

def show_bonus_text():
    cvs.delete("BONUS")
    draw_txt("BONUS +10!", 312, 100, 32, "red", "BONUS")
    root.after(1000, hide_bonus_text)  # 1초 후에 보너스 문구 삭제

def hide_bonus_text():
    cvs.delete("BONUS")


# 함수 영역
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

# 공간정보 저장
neko = []
check = []
for i in range(12):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

blockCount = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def draw_effect():
    cvs.delete("EFFECT")
    for y in range(12):
        for x in range(10):
            if destroyed[y][x] == 1:
                cvs.create_image(x * 58 + 40, y * 58 + 40, image=img_neko[7], tag="EFFECT")
    root.after(150, lambda: cvs.delete("EFFECT"))  # 0.3초 후 이펙트 삭제

def draw_neko(): 
    cvs.delete("NEKO")  # 캔버스에서 "NEKO"을 삭제
    for y in range(12): # 세로
        for x in range(10): # 가로
            if neko[y][x] > 0: # 모든 칸에 대해서 실행
                cvs.create_image(x * 58 + 40, y * 58 + 40, image=img_neko[neko[y][x]], tag="NEKO") # "NEKO" 생성

def check_neko():
    for y in range(12):
        for x in range(10): # 모든 칸에 대해서 실행
            check[y][x] = neko[y][x] # neko -> check (복사)
            
    def is_joker(block):
        return block == 8

    def get_joker_group(y, x):
        dirs = [(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(-1,1),(1,-1),(1,1)]
        neighbor_blocks = []
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 12 and 0 <= nx < 10:
                b = check[ny][nx]
                if b != 0 and b != 8:
                    neighbor_blocks.append(b)
        from collections import Counter
        c = Counter(neighbor_blocks)
        for block_type, count in c.items():
            if count >= 2:
                return block_type
        return 0

    for y in range(12):
        for x in range(10):
            if is_joker(check[y][x]):
                block_type = get_joker_group(y, x)
                if block_type != 0:
                    # 조커도 파괴
                    neko[y][x] = 9

                    # 주변에 같은 종류 블럭이 2개 이상일 경우 모두 파괴
                    dirs = [(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(-1,1),(1,-1),(1,1)]
                    for dy, dx in dirs:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < 12 and 0 <= nx < 10:
                            if neko[ny][nx] == block_type:
                                neko[ny][nx] = 9

    for y in range(1, 11):
        for x in range(9): # 맨 위와 맨 아래줄을 제외한 모든 칸에 대해서 실행
            if check[y][x] > 0: #세로 블럭
                if is_match(check[y-1][x], check[y][x]) and is_match(check[y][x], check[y+1][x]):
                    blockCount[neko[y][x]] += 3
                    neko[y - 1][x] = 9
                    neko[y][x] = 9
                    neko[y + 1][x] = 9

    for y in range(12):
        for x in range(1, 9): # 맨 왼쪽과 맨 오른쪽을 제외한 모든 칸에 대해서 실행
            if check[y][x] > 0: #가로 블럭
                if is_match(check[y][x], check[y][x-1]) and is_match(check[y][x], check[y][x+1]):
                    neko[y][x - 1] = 9
                    neko[y][x] = 9
                    neko[y][x + 1] = 9

    for y in range(1, 11):
        for x in range(1, 9): 
            if check[y][x] > 0: #대각선 블럭
                if is_match(check[y-1][x-1], check[y][x]) and is_match(check[y+1][x+1], check[y][x]):
                    neko[y - 1][x - 1] = 9
                    neko[y][x] = 9
                    neko[y + 1][x + 1] = 9
                if is_match(check[y+1][x-1], check[y][x]) and is_match(check[y-1][x+1], check[y][x]):
                    neko[y + 1][x - 1] = 9
                    neko[y][x] = 9
                    neko[y - 1][x + 1] = 9

    for y in range(0, 11):
        for x in range(0, 9): 
            if check[y][x] > 0:
                if is_match(check[y + 1][x], check[y][x]) and is_match(check[y + 1][x + 1], check[y][x]) and is_match(check[y - 1][x], check[y][x]):
                    neko[y - 1][x] = 9
                    neko[y][x + 1] = 9
                    neko[y + 1][x] = 9
                    neko[y + 1][x + 1] = 9
        # 2x2 정사각형 체크 추가
    for y in range(11):  # 0~8까지 (y+1이 9까지만 되도록)
        for x in range(9):  # 0~6까지 (x+1이 7까지만 되도록)
            if check[y][x] > 0:
                if is_match(check[y][x], check[y][x+1]) and is_match(check[y][x], check[y+1][x]) and is_match(check[y][x], check[y+1][x+1]):
                    neko[y][x] = 9
                    neko[y][x+1] = 9
                    neko[y+1][x] = 9
                    neko[y+1][x+1] = 9


def reset_game_loop_flag():
    global game_loop_running
    game_loop_running = False
    game_main()

def sweep_neko():
    global blockCount
    num = 0
    for y in range(12):
        for x in range(9):# 모든 칸에 대해서 실행
            if neko[y][x] == 9:
                neko[y][x] = 0   # 빈칸
                num = num + 1    # 파괴된 블럭 개수를 표현
    print("blockCount :", blockCount)
    return num

def drop_neko():
    flg = False
    for y in range(10, -1, -1): #아래에서 위로 검사
        for x in range(10): #모든 블럭에 대해서 검사
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():
    for x in range(10):
        if neko[0][x] > 0: # 맨 윗줄에 블럭이 있으면
            return True # 게임 종료
    return False

def set_neko():
    for x in range(10):
        neko[0][x] = random.randint(0, difficulty) # 블럭을 생성 (0 빈, 1~6 일반블럭)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def is_match(a, b): #조커함수
    # 8번은 조커 블럭
    return a == b and a != 8 and b != 8

def game_main():
    global index, timer, score, hisc, difficulty, tsugi, tmr, timer_active, no_input_time, game_loop_running, joker_count, joker_pending, new_joker_pending
    global cursor_x, cursor_y, mouse_c
    if game_loop_running:
        return
    game_loop_running = True
    ...
    root.after(100, reset_game_loop_flag)

    if index == 0:  # 타이틀 로고
        cvs.delete("ALL")  # 모든 캔버스 요소 제거
        cvs.create_image(456, 384, image=bg)  # ← 배경 재표시
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        index = 1
        mouse_c = 0
        tmr = 0
        cvs.delete("TIMER")
    elif index == 1:  # 타이틀 화면, 시작 대기
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x and mouse_x < 456 and 384 < mouse_y and mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x and mouse_x < 456 and 528 < mouse_y and mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x and mouse_x < 456 and 672 < mouse_y and mouse_y < 744:
                difficulty = 6
        if difficulty > 0:
            for y in range(12):
                for x in range(10):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            tmr = 0
            timer_active = True  
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            root.after(1000, countUp)
            index = 2
    elif index == 2:  # 블록 낙하
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3:  # 나란히 놓인 블록 확인
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:  # 나란히 놓인 고양이 블록이 있다면
        sc = sweep_neko()
        score = score + sc * difficulty * 2
        if score > hisc:
            hisc = score
        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                index = 5
            else:
                index = 6
                timer = 0
        if sc >= 10:
            score += 10
            show_bonus_text()   # 보너스 문구 함수 호출
        if score > hisc:
            hisc = score
        if sc > 0:
            draw_effect()
            index = 2 # 블록 떨어뜨리는 단계로
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                index = 5 # 다음 블록 놓기 대기
            else:
                index = 6 # 게임 오버
                timer = 0
        draw_neko()

        new_joker_pending = []
        for y, x in joker_pending:
            if neko[y][x] == 9 or neko[y][x] == 0:
            # 조커가 부서져서 이미 없거나, 빈칸이면 아무 처리 안 함
                continue
            else:
            # 조커가 아직 남아있으면 랜덤 일반블럭으로 바꿈
                neko[y][x] = random.randint(1, difficulty)
        joker_pending.clear()
        
    elif index == 5:  # 마우스 입력 대기
        no_input_time += 1  # 입력 없는 시간 증가

        if 12 <= mouse_x and mouse_x < 12 + 60 * 10 and 12 <= mouse_y and mouse_y < 12 + 60 * 12:
            cursor_x = int((mouse_x - 12) / 60) # 칸 수 만큼 입력0 ~ 7
            cursor_y = int((mouse_y - 12) / 60) # 칸 수 만큼 입력0 ~ 9
            if mouse_c == 1:
                mouse_c = 0
                joker_count += 1
                
                if joker_count >= 5:
                    tsugi = 8  # 조커 블럭 (코드 8번)
                    joker_count = 0
                
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                if tsugi == 8:
                    joker_pending.append((cursor_y, cursor_x))  # 조커 위치 기록
                tsugi = 0
                no_input_time = 0
                index = 2
            else:
                # 마우스가 범위 밖에 있을 때도 시간은 흐르도록 허용
                
                # # 5초(100ms * 50) 이상 입력 없을 경우 자동 배치
                if no_input_time >= 50 and tsugi > 0:
                    for y in range(9, -1, -1):
                        if neko[y][cursor_x] == 0:
                            set_neko()
                            neko[y][cursor_x] = tsugi
                            tsugi = 0
                            no_input_time = 0
                            index = 2
                            break
                        
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 58 + 40, cursor_y * 58 + 40, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:  # 게임 오버
        timer = timer + 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
            save_hisc()  # 게임 오버 시점에 최고점 저장
            timer_active = False  # 타이머 중지
        if timer == 50:
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 450, 60, 32, "yellow", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

def esc_pressed(e): # 게임 종료 버튼
    global index, tmr, timer, timer_active, score, tsugi, cursor_x, cursor_y, mouse_c
    if 2 <= index <= 5:
        answer = tkinter.messagebox.askyesno("확인", "게임을 종료하시겠습니까?")
        if answer:
            index = 0
            tmr = 0
            timer = 0
            timer_active = False  # 타이머 중지
            score = 0
            tsugi = 0
            mouse_c = 0
            cursor_x = 0
            cursor_y = 0
            cvs.delete("TIMER")
            cvs.delete("CURSOR")
            cvs.delete("INFO")
            cvs.delete("NEKO")
            game_main()
            

def sweep_neko():
    global blockCount, destroyed
    num = 0

    for y in range(12):
        for x in range(10):
            destroyed[y][x] = 0  # 매 턴 초기화

    for y in range(12):
        for x in range(10):
            if neko[y][x] == 9:
                destroyed[y][x] = 1  # 파괴 기록
                neko[y][x] = 0
                num += 1

    print("blockCount :", blockCount)
    return num


# 메인 영역
root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<Escape>", esc_pressed)
cvs = tkinter.Canvas(root, width=912, height=768)
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
    tkinter.PhotoImage(file="neko_joker.png")
] # 블록 이미지

while len(img_neko) < 20:
    img_neko.append(None)

cvs.create_image(456, 384, image=bg)
cvs.delete("BONUS")
# 최고점수 불러오기load_hisc()
game_main()
root.mainloop()