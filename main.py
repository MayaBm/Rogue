import curses
stdscr = curses.initscr()
stdscr.keypad(True)
from personnage import Personnage
from monstre import Monstre
from tresor import Tresor

MAX_X = 10
MAX_Y = 10
perso = Personnage()
monstre = Monstre()
tres = Tresor()
#potentiellememt : creer une liste de tresor

while (True):
    depl = stdscr.getch()
    if depl == curses.KEY_UP and perso.py < MAX_Y - 1 :
        perso.py += 1
        print("UP")
    elif depl == curses.KEY_DOWN and perso.py > 0:
        perso.py -= 1
        print("DOWN")
    elif depl == curses.KEY_LEFT and perso.px > 0:
        perso.px -=1
        print("LEFT")
    elif depl == curses.KEY_RIGHT and perso.px < MAX_X - 1:
        perso.px +=1
        print("RIGHT")    
    if perso.get_position() == monstre.get_position() :
        monstre.pv -=1
        print("monstre mort")
        print(tres.get_position())
    if perso.get_position() == tres.get_position() :
        tres.output = False
        print("tresor trouve")
    if not tres.output and monstre.get_pv == 0 :
        break    