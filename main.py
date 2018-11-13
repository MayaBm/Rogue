import curses, fenetre, numpy
from personnage import Personnage
from monstre import Monstre
from tresor import Tresor

i = 1
stdscr = curses.initscr()
stdscr.keypad(True)
stdscr = curses.initscr()
begin_x = 20; begin_y = 7
height = 5; width = 40
case = numpy.zeros( (5,40) )
case[3,3]= 1
win = curses.newwin(30, 30, 30, 30)

MAX_X = 5
MAX_Y = 40
perso = Personnage()
monstre = Monstre()
tres = Tresor()
#potentiellememt : creer une liste de tresor

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
    depl = stdscr.getch()
    if depl == curses.KEY_RIGHT and perso.py < MAX_Y - 1 :
        i,j=perso.get_position()
        case[i,j]=0
        perso.py += 1
        i,j=perso.get_position()
        case[i,j]=1
    elif depl == curses.KEY_LEFT and perso.py > 0:
        i,j=perso.get_position()
        case[i,j]=0
        perso.py -= 1
        i,j=perso.get_position()
        case[i,j]=1
    elif depl == curses.KEY_DOWN and perso.px < MAX_X - 1:
        i,j=perso.get_position()
        case[i,j]=0
        perso.px += 1
        i,j=perso.get_position()
        case[i,j]=1
    elif depl == curses.KEY_UP and perso.px > 0 :
        i,j=perso.get_position()
        case[i,j]=0
        perso.px -= 1
        i,j=perso.get_position()
        case[i,j]=1
    if perso.get_position() == monstre.get_position() :
        monstre.pv -=1
        print("monstre mort")
        print(tres.get_position())
    if perso.get_position() == tres.get_position() :
        tres.output = False
        print("tresor trouve")
    if not tres.output and monstre.get_pv == 0 :
        break    