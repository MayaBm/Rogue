import random
class Tresor:
    def __init__(self):
        self.output = True
        self.px = int(10*random.random())
        self.py = int(10*random.random())


    def get_position(self):
        return(self.px, self.py)


    #def on(self):
    # display icon

    #def off(self):
    # remove icon ft



