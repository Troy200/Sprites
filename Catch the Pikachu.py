import pgzrun
import random

WIDTH=900
HEIGHT=800

x="light blue"

Ash=Actor("ash ketchum game 2")
Pika=Actor("pikachu_game_removebg")
Pika.pos=300,250

Points=0

game_over= False
def time_up():
    global game_over
    game_over=True


def update():
    global Points
    if keyboard.A:
        Ash.x = Ash.x-2
    if keyboard.D:
        Ash.x =Ash.x + 2
    if keyboard.W:
        Ash.y=Ash.y -2
    if keyboard.S:
         Ash.y=Ash.y +2

    
    if Ash.colliderect(Pika):
        x=random.randint(5,895)
        y=random.randint(5,795)
        Pika.pos=x,y

        Points=Points+1


def draw():
    screen.fill(x)
    Ash.draw()
    Pika.draw()
    screen.draw.text(str(Points),(880,780))
    
    if game_over==True:
        screen.fill("red")
      
        
clock.schedule(time_up, 40.0)

pgzrun.go()