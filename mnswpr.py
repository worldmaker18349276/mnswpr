import curses, numpy

def main():
    size = (15, 25)
    ratio = 0.2

    try:
        scr = curses.initscr()
        scr.keypad(1)
        curses.mousemask(1)

        mines = numpy.pad(numpy.random.rand(*size) < ratio, 1)
        board = numpy.pad(numpy.full(size, 9), 1)
        while True:
            scr.addstr(1, 0, str(board[1:-1,1:-1]).replace("9", " "))
            if (board[~mines] != 9).all(): break
            if scr.getch() != curses.KEY_MOUSE: continue
            x, y = curses.getmouse()[1:3]
            p = [(y, x//2)]
            for y, x in p:
                if mines[y,x]: board[:] = 0
                if board[y,x] != 9: continue
                around = numpy.indices((3,3)).reshape(2,-1).T - 1 + [y,x]
                board[y,x] = mines[tuple(around.T)].sum()
                if board[y,x] == 0: p += [*around]

        scr.addstr("END")
        scr.getch()

    finally:
        curses.endwin()
