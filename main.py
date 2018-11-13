import curses, fenetre, numpy
from personnage import Personnage
from monstre import Monstre
from tresor import Tresor

i = 1
end = True
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


i,j= monstre.get_position() 
case[i,j]=2          #affichage monstre

i,j= tres.get_position() 
case[i,j]=3


while (end):
    curses.noecho()
    # stdscr.clear()
    for i in range (5):
        for j in range (40):
            if case[i,j] == 0:
                stdscr.addstr(i,j, ".")
            elif case[i,j] == 1:
                stdscr.addstr(i,j, "X\n")
            elif case[i,j] == 2:
                stdscr.addstr(i,j, "M\n")
            elif case[i,j] == 3:
                stdscr.addstr(i,j, "T\n")
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
        monstre.pv -= 1
    if perso.get_position() == tres.get_position() :
        tres.output = False
        case[i,j] = 1
    if (monstre.get_pv() < 1 and tres.output == False) :
        break
        curses.endwin()