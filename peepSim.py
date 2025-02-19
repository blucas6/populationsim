import pygame
import sys
import colors as C
import peep as P
import random as rand
import text as T

def tracker(p):
    global blue_males
    global blue_females
    global red_males
    global red_females
    if p.color == 1:
        if p.sex == 1:
            blue_males += 1
        else: 
            blue_females += 1
    elif p.color == 2:
        if p.sex == 1:
            red_males += 1
        else:
            red_females += 1

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Peep Simulation')

screenx = 500
screeny = 400

screen = pygame.display.set_mode((screenx+10, screeny+10))

peeplist = pygame.sprite.Group()
peeplist.add(P.Peep(screen, 1, 1, rand.randint(0, screenx), rand.randint(0, screeny), P.norm([-1, 1]), screenx, screeny))
peeplist.add(P.Peep(screen, 0, 1, rand.randint(0, screenx), rand.randint(0, screeny), P.norm([-1, 1]), screenx, screeny))
peeplist.add(P.Peep(screen, 1, 2, rand.randint(0, screenx), rand.randint(0, screeny), [0, 1], screenx, screeny))
peeplist.add(P.Peep(screen, 0, 2, rand.randint(0, screenx), rand.randint(0, screeny), [0, -1], screenx, screeny))
peeplist.add(P.Peep(screen, 1, 3, rand.randint(0, screenx), rand.randint(0, screeny), [0, 1], screenx, screeny))
peeplist.add(P.Peep(screen, 0, 3, rand.randint(0, screenx), rand.randint(0, screeny), [0, -1], screenx, screeny))
peeplist.add(P.Peep(screen, 1, 4, rand.randint(0, screenx), rand.randint(0, screeny), [0, 1], screenx, screeny))
peeplist.add(P.Peep(screen, 0, 4, rand.randint(0, screenx), rand.randint(0, screeny), [0, -1], screenx, screeny))

blue_males = 1
blue_females = 1
red_males = 1
red_females = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(C.white)

    text1 = T.Text("Amount of Blue: "+str(blue_males+blue_females)+" (M"+str(blue_males)+") (F"+str(blue_females)+")", (0, 0), 20, C.black)
    text2 = T.Text("Amount of Red: "+str(red_males+red_females)+" (M"+str(red_males)+") (F"+str(red_females)+")", (0, 20), 20, C.black)
    text1.draw(screen)
    text2.draw(screen)

    blue_males = 0
    blue_females = 0
    red_males = 0
    red_females = 0

    for p in peeplist:
        tracker(p)
        peeplist.remove(p)
        p.checkCollision(peeplist)
        peeplist.add(p)

    peeplist.update(peeplist)
    peeplist.draw(screen)

    pygame.display.flip()
    clock.tick(59)