import random
import curses

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def spawn():
    empty = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty.append((i, j))
    if empty:
        r, c = random.choice(empty)
        board[r][c] = 2

def shift_left(row):
    new = [0, 0, 0, 0]
    idx = 0
    for x in row:
        if x != 0:
            new[idx] = x
            idx += 1
    return new

def merge_left(row):
    for i in range(3):
        if row[i] != 0 and row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left():
    for i in range(4):
        r = shift_left(board[i])
        r = merge_left(r)
        r = shift_left(r)
        board[i] = r

def move_right():
    for i in range(4):
        r = board[i]
        r.reverse()
        r = shift_left(r)
        r = merge_left(r)
        r = shift_left(r)
        r.reverse()
        board[i] = r

def move_up():
    for col in range(4):
        r = [board[x][col] for x in range(4)]
        r = shift_left(r)
        r = merge_left(r)
        r = shift_left(r)
        for x in range(4):
            board[x][col] = r[x]

def move_down():
    for col in range(4):
        r = [board[x][col] for x in range(4)]
        r.reverse()
        r = shift_left(r)
        r = merge_left(r)
        r = shift_left(r)
        r.reverse()
        for x in range(4):
            board[x][col] = r[x]

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

def draw(scr):
    scr.clear()
    scr.addstr(0, 0, "2048 Game")
    scr.addstr(1, 0, "W A S D = move | Q = quit")

    y = 3
    for i in range(4):
        line = ""
        for j in range(4):
            line += str(board[i][j]).rjust(5)
        scr.addstr(y, 0, line)
        y += 1

    scr.refresh()

def main(scr):
    curses.curs_set(0)

    spawn()
    spawn()

    while True:
        draw(scr)
        key = scr.getch()

        try:
            c = chr(key).lower()
        except:
            continue

        moved = False

        if c == "q":
            break
        elif c == "a":
            move_left()
            moved = True
        elif c == "d":
            move_right()
            moved = True
        elif c == "w":
            move_up()
            moved = True
        elif c == "s":
            move_down()
            moved = True

        if moved:
            spawn()
            if not can_move():
                draw(scr)
                scr.addstr(9, 0, "GAME OVER!!!!! Press any key.")
                scr.refresh()
                scr.getch()
                break

curses.wrapper(main)
