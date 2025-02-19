import pygame
import random as rand
import math
import text as T
import colors as C

class Peep(pygame.sprite.Sprite):
    def __init__(self, surface, sex, color, x, y, dir, screenx, screeny):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.sex = sex
        self.color = color
        self.dir = dir
        self.screenx = screenx
        self.screeny = screeny
        self.birth_timer = 100
        self.life_timer = 3000
        if color == 1:
            if sex == 1:
                self.image = pygame.image.load("peepsprite/male_blue.png")
            else:
                self.image = pygame.image.load("peepsprite/female_blue.png")
        elif color == 2:
            if sex == 1:
                self.image = pygame.image.load("peepsprite/male_red.png")
            else:
                self.image = pygame.image.load("peepsprite/female_red.png")
        elif color == 3:
            if sex == 1:
                self.image = pygame.image.load("peepsprite/male_green.png")
            else:
                self.image = pygame.image.load("peepsprite/female_green.png")
        else:
            if sex == 1:
                self.image = pygame.image.load("peepsprite/male_yellow.png")
            else:
                self.image = pygame.image.load("peepsprite/female_yellow.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self, peeplist):    
        if self.birth_timer > 0:
            self.birth_timer -= 1
        if self.life_timer > 0:
            self.life_timer -= 1
        if self.life_timer == 0:
            peeplist.remove(self)
        self.dir[0] = round(self.dir[0])
        self.dir[1] = round(self.dir[1])
        self.rect.x += self.dir[0]
        self.rect.y += self.dir[1]
        if self.rect.x <= 0 or self.rect.x >= self.screenx:
            self.dir[0] *= -1
        
        if self.rect.y <= 0 or self.rect.y >= self.screeny:
            self.dir[1] *= -1

    def checkCollision(self, peeplist):
        col_obj = pygame.sprite.spritecollide(self, peeplist, False)
        if len(col_obj) != 0:
            v = [col_obj[0].rect.x - self.rect.x, col_obj[0].rect.y - self.rect.y]
            v[0] = v[0] * -1
            v[1] = v[1] * -1
            self.dir = norm(v)
            if self.sex == 1 and col_obj[0].sex == 0:
                if self.birth_timer == 0:
                    self.birth(peeplist)
                    self.birth_timer = 100

    def birth(self, peeplist):
        v = [rand.randint(-10, 10), rand.randint(-10, 10)]
        rand_dir = norm(v)
        sex = rand.randint(0, 1)
        newPeep = Peep(self.surface, sex, self.color, self.rect.x+10, self.rect.y+10, rand_dir, self.screenx, self.screeny)
        peeplist.add(newPeep)
            

    # def draw(self):

    #     pygame.draw.circle(self.surface, self.color, (self.posx, self.posy), self.size)
    #     if self.sex == 1:
    #         tag = T.Text("M", (self.posx-5, self.posy-7), 23, C.black)
    #         tag.draw(self.surface)
    #     else:
    #         tag = T.Text("F", (self.posx-5, self.posy-7), 23, C.black)
    #         tag.draw(self.surface)
    
    # def update(self):
    #     if self.birth_timer > 0:
    #         self.birth_timer -= 1
    #     self.posx += self.dir[0]
    #     self.posy += self.dir[1]
    
    # def detect_col(self, screenx, screeny, peeplist):
    #     for p in peeplist:
    #         if not p is self:
    #             if abs(p.posx - self.posx) < self.size+5 and abs(p.posy - self.posy) < self.size+5:
    #                 v = [p.posx - self.posx, p.posy - self.posy]
    #                 v[0] = v[0] * -1
    #                 v[1] = v[1] * -1
    #                 self.dir = norm(v)
    #                 if self.sex == 1 and p.sex == 0:
    #                     if self.birth_timer == 0:
    #                         self.birth(peeplist)
    #                         self.birth_timer = 100

    #     if self.posx - self.size <= 0 or self.posx + self.size >= screenx:
    #         self.dir[0] *= -1
        
    #     if self.posy - self.size <= 0 or self.posy + self.size >= screeny:
    #         self.dir[1] *= -1
    



def norm(v):
    mag = math.sqrt(v[0]*v[0] + v[1]*v[1])
    if mag > 0:
        v[0] = v[0] / mag
    if mag > 0:
        v[1] = v[1] / mag
    return v



