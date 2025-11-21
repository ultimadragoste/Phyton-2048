import random

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def print_board():
    print("==========")
    for row in board:
        print(row)
    print("==========")

def spawn():
    empty = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty.append((i, j))
    if empty:
        r, c = random.choice(empty)
        board[r][c] = 2

def merge_row_left(row):
    new = []
    for x in row:
        if x != 0:
            new.append(x)

    merged = []
    i = 0
    while i < len(new):
        if i + 1 < len(new) and new[i] == new[i+1]:
            merged.append(new[i] * 2)
            i += 2
        else:
            merged.append(new[i])
            i += 1

    while len(merged) < 4:
        merged.append(0)

    return merged

def move_left():
    for i in range(4):
        board[i] = merge_row_left(board[i])

def move_right():
    for i in range(4):
        board[i].reverse()
        board[i] = merge_row_left(board[i])
        board[i].reverse()

def move_up():
    for col in range(4):
        column = [board[0][col], board[1][col], board[2][col], board[3][col]]
        merged = merge_row_left(column)
        for row in range(4):
            board[row][col] = merged[row]

def move_down():
    for col in range(4):
        column = [board[0][col], board[1][col], board[2][col], board[3][col]]
        column.reverse()
        merged = merge_row_left(column)
        merged.reverse()
        for row in range(4):
            board[row][col] = merged[row]

def can_move():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1]:
                return True
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j]:
                return True
    return False





spawn()
spawn()
print_board()

while True:
    cmd = input("Move use (W/A/S/D), Q for quit: ").lower()

    if cmd == "q":
        break
    elif cmd == "a":
        move_left()
        spawn()
    elif cmd == "d":
        move_right()
        spawn()
    elif cmd == "w":
        move_up()
        spawn()
    elif cmd == "s":
        move_down()
        spawn()
    else:
        print("Wrong Input!")

    print_board()

    if not can_move():
        print("GAME OVER! No More Moves!!!!.")
        break
