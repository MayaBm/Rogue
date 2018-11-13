import random

if monstre.get_pv() > 0 : #tant que le monstre est en vie
    if abs(monstre.py - perso.py) < 2 and abs(monstre.px - perso.px) < 2 :
        perso.pv -= 1
        print ("PV : " + perso.get_pv())
    else : 
        deplm = random.randint(0,4)
        if deplm == 0 and monstre < MAX_Y - 1 :
            i,j=monstre.get_position()
            case[i,j]=0
            monstre.py += 1
            i,j=monstre.get_position()
            case[i,j]=2
        elif deplm == 1 and monstre.py > 0:
            i,j=monstre.get_position()
            case[i,j]=0
            monstre.py -= 1
            i,j=monstre.get_position()
            case[i,j]=2
        elif deplm == 2 and monstre.px < MAX_X - 1:
            i,j=monstre.get_position()
            case[i,j]=0
            monstre.px += 1
            i,j=monstre.get_position()
            case[i,j]=2
        elif deplm == 3 and monstre.px > 0 :
            i,j=monstre.get_position()
            case[i,j]=0
            monstre.px -= 1
            i,j=monstre.get_position()
            case[i,j]=2