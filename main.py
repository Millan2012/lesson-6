import pgzrun
from random import randint
WIDTH=800
HEIGHT=600
option=int(input("1=easy,2=medium,3=hard"))
if option==1:
    total=5
elif option==2:
    total=10
elif option==3:
    total=15
sats=[]
for i in range (total):

    sat=Actor("satellite")

    sat.x=randint(50,WIDTH-50)
    sat.y=randint(50,HEIGHT-50)
    sats.append(sat)

def draw():
    screen.blit("space",(0,0))
    num=1
    for sat in sats:
        sat.draw()
        screen.draw.text(str(num),(sat.x,sat.y+35))
        num=num+1
pgzrun.go()