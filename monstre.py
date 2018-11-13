class Monstre:
    def __init__(self):
        self.pv = 1
        self.px = 5
        self.py = 5

    def get_position(self):
        return(self.px, self.py)
    
    def get_pv(self):
        return(self.pv)