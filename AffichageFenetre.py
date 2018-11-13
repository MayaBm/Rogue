import curses, fenetre
import numpy
stdscr = curses.initscr()
begin_x = 20; begin_y = 7
height = 5; width = 40
case = numpy.zeros( (5,40) )
case[2,3]= 1
win = curses.newwin(30, 30, 30, 30)
while (True):
    curses.noecho()
    # stdscr.clear()
    for i in range (5):
        for j in range (40):
            if case[i,j] == 0:
                stdscr.addstr(i,j, "0")
            elif case[i,j] == 1:
                stdscr.addstr(i,j, "X\n")
    win.border(0)
    stdscr.refresh()
