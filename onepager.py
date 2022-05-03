# pip install mnswpr

import curses as cs, numpy as np
sz, r = (15, 25), 0.2
s = cs.initscr()
s.keypad(1)
cs.mousemask(1)
mn = np.pad(np.random.rand(*sz) < r, 1)
bd = np.pad(np.full(sz, 9), 1)
while 1:
    s.addstr(1, 0, str(bd[1:-1,1:-1]).replace("9", " "))
    if (bd[~mn] != 9).all(): break
    if s.getch() != cs.KEY_MOUSE: continue
    x, y = cs.getmouse()[1:3]
    p = [(y, x//2)]
    for y, x in p:
        if mn[y,x]: bd[:] = 0
        if bd[y,x] != 9: continue
        a = np.indices((3,3)).reshape(2,-1).T-1+[y,x]
        bd[y,x] = mn[tuple(a.T)].sum()
        if bd[y,x] == 0: p += [*a]
