import curses

class Fenetre:
    
    def _init_ (self):
        self.lignes = 5
        self.cols = 10
        self.pos = [10,10]

    # def init_curses(lignes,cols,pos):
    # curses.initscr()
    # curses.noecho()
    # curses.cbreak()
    # curses.curs_set(0)

    # window = curses.newwin(lignes,cols,pos[0],pos[1])
    # window.border(0)
    # window.keypad(1)
    # return window

    # def close_curses():
    #     curses.echo()
    #     curses.nocbreak()
    #     curses.curs_set(1)
    #     curses.endwin()

