import pgzrun
import random


WIDTH=600
HEIGHT=500

Bee=Actor("bee")
Bee.pos=300,250

Flower=Actor("flower")

Points=0

game_over= False

def time_up():
    global game_over
    game_over=True


def update():
    global Points
    if keyboard.left:
        Bee.x = Bee.x-2
    if keyboard.right:
        Bee.x =Bee.x + 2
    if keyboard.up:
        Bee.y=Bee.y -2
    if keyboard.down:
         Bee.y=Bee.y +2
    if Bee.colliderect(Flower):

        x=random.randint(5,595)
        y=random.randint(5,495)
        Flower.pos=x,y

        Points=Points+1



def draw():
    screen.blit("background",(0,0))
    Bee.draw()
    Flower.draw()
    screen.draw.text(str(Points),(580,480))
    
    if game_over==True:
        screen.fill("red")



clock.schedule(time_up, 10.0)



pgzrun.go()