import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
HOLD_WIDTH = 6 * GRID_SIZE
NEXT_WIDTH = 6 * GRID_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH + HOLD_WIDTH + NEXT_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

colors = [CYAN, BLUE, ORANGE, YELLOW, GREEN, MAGENTA, RED]

# 게임 보드 크기 설정
BOARD_WIDTH = SCREEN_WIDTH // GRID_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 테트리스 블록 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]]
]

class Block:
    saved = False

    def __init__(self, shape=None):
        self.shape = shape if shape else random.choice(SHAPES)
        self.color = random.choice(colors)
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0


def draw_block(block, offset_x=0, offset_y=0):
    for i, row in enumerate(block.shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, block.color, pygame.Rect((block.x + j + offset_x) * GRID_SIZE, (block.y + i + offset_y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_board(board):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x]:
                pygame.draw.rect(screen, board[y][x], pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# 게임 보드 초기화
board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def check_collision(board, block, dx=0, dy=0):
    for i, row in enumerate(block.shape):
        for j, cell in enumerate(row):
            if cell:
                if i + block.y + dy >= BOARD_HEIGHT or \
                   j + block.x + dx < 0 or j + block.x + dx >= BOARD_WIDTH or \
                   board[i + block.y + dy][j + block.x + dx]:
                    return True
    return False

def clear_lines(board):
    full_lines = 0
    for y in range(BOARD_HEIGHT):
        if all(board[y]):
            del board[y]
            board.insert(0, [0 for _ in range(BOARD_WIDTH)])
            full_lines += 1
    return full_lines

def freeze_block(board, block):
    for i, row in enumerate(block.shape):
        for j, cell in enumerate(row):
            if cell:
                board[i + block.y][j + block.x] = block.color
    lines_cleared = clear_lines(board)
    return lines_cleared

def rotate_block_cw(block):
    block.shape = [list(row) for row in zip(*block.shape[::-1])]

def rotate_block_ccw(block):
    block.shape = [list(row) for row in zip(*block.shape)]
    block.shape.reverse()

def rotate_block_180(block):
    rotate_block_cw(block)
    rotate_block_cw(block)

def handle_keys(event, block, hold_block, held):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if not check_collision(board, block, dx=-1):
                block.x -= 1
        elif event.key == pygame.K_RIGHT:
            if not check_collision(board, block, dx=1):
                block.x += 1
        elif event.key == pygame.K_DOWN:
            if not check_collision(board, block, dy=1):
                block.y += 1
        elif event.key == pygame.K_UP:
            rotate_block_cw(block)
            if check_collision(board, block):
                for _ in range(3):
                    rotate_block_cw(block)
        elif event.key == pygame.K_z:
            rotate_block_ccw(block)
            if check_collision(board, block):
                for _ in range(3):
                    rotate_block_ccw(block)
        elif event.key == pygame.K_x:
            rotate_block_180(block)
            if check_collision(board, block):
                for _ in range(2):
                    rotate_block_cw(block)
        elif event.key == pygame.K_c:
            if not held:
                print(hold_block.saved)
                if hold_block.shape :
                    block, hold_block = hold_block, block
                    block.x = BOARD_WIDTH // 2 - len(block.shape[0]) // 2
                    block.y = 0
                    hold_block.saved = True
                else:
                    hold_block = block
                    block = next_blocks.pop(0)
                    block.x = BOARD_WIDTH // 2 - len(block.shape[0]) // 2
                    block.y = 0
                    next_blocks.append(Block())
                    hold_block.saved = False
                held = True

    return hold_block, held

def draw_hold(hold_block):
    if hold_block.shape:
        offset_x = BOARD_WIDTH + 1
        offset_y = 1
        for i, row in enumerate(hold_block.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, hold_block.color, pygame.Rect((j + offset_x) * GRID_SIZE, (i + offset_y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_next(next_blocks):
    offset_x = BOARD_WIDTH + 1 + 6
    for index, block in enumerate(next_blocks):
        offset_y = 4 * index + 1
        for i, row in enumerate(block.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, block.color, pygame.Rect((j + offset_x) * GRID_SIZE, (i + offset_y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    global next_blocks
    clock = pygame.time.Clock()
    block = Block()
    next_blocks = [Block() for _ in range(4)]
    hold_block = Block(shape=[])
    held = False
    fall_time = 0
    fall_speed = 500
    score = 0

    running = True
    while running:
        screen.fill(BLACK)

        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time >= fall_speed:
            if not check_collision(board, block, dy=1):
                if held == False :
                    block.y += 1
                else :
                    block = next_blocks.pop(0)
                    block.x = BOARD_WIDTH // 2 - len(block.shape[0]) // 2
                    block.y = 0
                    next_blocks.append(Block())
                    held = False
            else:
                lines_cleared = freeze_block(board, block)
                score += lines_cleared * 100
                block = next_blocks.pop(0)
                block.x = BOARD_WIDTH // 2 - len(block.shape[0]) // 2
                block.y = 0
                next_blocks.append(Block())
                if check_collision(board, block):
                    running = False
                held = False
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            hold_block, held = handle_keys(event, block, hold_block, held)

        draw_board(board)
        draw_block(block)
        draw_hold(hold_block)
        draw_next(next_blocks)

        # 점수 표시
        font = pygame.font.SysFont('Arial', 25)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
