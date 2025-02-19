import pygame

class Text():
    def __init__(self, text, pos, fontsz, color):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = fontsz
        self.fontcolor = color
        self.set_font()
        self.render()
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    def draw(self, screen):
        screen.blit(self.img, self.rect)