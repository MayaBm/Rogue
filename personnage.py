class Personnage:
    def __init__(self):
        self.pv = 12
        self.px = 3
        self.py = 3

    def get_position(self):
        return(self.px, self.py)
    
    def get_pv(self):
        return(self.pv)
