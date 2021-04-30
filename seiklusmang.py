import pygame
import sys
from easygui import *
import random
from EasyGUI_Skairem import *

pygame.init()

pygame.display.set_caption("Seiklusmäng")
screen = pygame.display.set_mode((960, 720))

#Maailma ehitus kahemõõtmelise järjendina

taust1 =  pygame.image.load("Pildid/taustv1.jpg").convert_alpha()
map = [
       [1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,taust1,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]
       ]
#--------------------------------------------------------------------------------------------------------------------------------
HP = 100
eluvarv = 255,0,0
possa_elu = 50
gapple = False
mook = False

TUTORIAL()
tegelane_pildid = valivarv()




def fight(dmg, tüüp):
    #if sprite collision cancer
    
    x = random.randint(1, 10)
    global HP
    enemy_HP = int(tüüp)
    if x == 1:
        msgbox("Lõid mööda ja vastane tabas sind -10HP")
        HP -= 10
    if x >= 2 and x <= 3:
        msgbox("Lõid mööda, kuida põikasid vastulöögi eest kõrvale")
    if x >= 4 and x <= 9:
        msgbox("Tabasid vastast!")
        enemy_HP -= dmg
    if x == 10:
        msgbox("Tabasid vastase nõrka punkti! Hea löök! ")
        enemy_HP -= (1.5*dmg)
    
    return int(enemy_HP)
    

def Quest1(): #done
     klahv = pygame.key.get_pressed()
     mook = False
     global gapple
     mullmull = Jutumull1()
     jutumull_grupp = pygame.sprite.Group()
     jutumull_grupp.add(mullmull)
     
     tehtud = Jutumull2()
     tehtud_grupp = pygame.sprite.Group()
     tehtud_grupp.add(tehtud)
     
     auhind= Jutumull3()
     auhind_grupp = pygame.sprite.Group()
     auhind_grupp.add(auhind)
     #if sprite collision
     if klahv[pygame.K_e] and gapple == False:
            mullmull.joonista(screen)
            mook = False
     if klahv[pygame.K_e] and gapple == True:
            tehtud.joonista(screen)
            auhind.joonista(screen)
            mook = True
            
     return mook
    

tegelane_pilt = pygame.transform.scale(tegelane_pildid[0], (64, 64))
tegelane_pilt_v = pygame.transform.scale(tegelane_pildid[1], (64, 64))
tekst1 = pygame.image.load("Pildid/LINES/Quest1.png").convert_alpha()
tekst2= pygame.image.load("Pildid/LINES/Quest1-complete.png").convert_alpha()
auhind1 = pygame.image.load("Pildid/LINES/Quest1-Reward.png").convert_alpha()
precomplete1 = pygame.transform.scale(tekst1, (429, 130))
postcomplete1 = pygame.transform.scale(tekst2, (396, 120))
reward1 = pygame.transform.scale(auhind1, (396,120))
#Jututututumulll
class Jutumull1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = precomplete1
        self.rect = self.image.get_rect()
        self.x = 144
        self.y = 144
    def joonista(self, surface):
        surface.blit(self.image,(self.x,self.y))

class Jutumull2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = postcomplete1
        self.rect = self.image.get_rect()
        self.x = 144
        self.y = 144
    def joonista(self, surface):
        surface.blit(self.image,(self.x,self.y))

class Jutumull3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = reward1
        self.rect = self.image.get_rect()
        self.x = 444
        self.y = 444
    def joonista(self, surface):
        surface.blit(self.image,(self.x,self.y))        
#------------------------------------------------------
#tegelase class (välimus, liikumine, animatsioon(varsti))
class Tegelane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = tegelane_pilt
        self.rect = self.image.get_rect()
        self.x = 450
        self.y = 250
        TegelaneX = self.x
        TegelaneY = self.y
    def joonista(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
    def liikumine(self):
        klahv = pygame.key.get_pressed()
        dist = 0.25
        if klahv[pygame.K_a] or klahv[pygame.K_LEFT]:
            self.x -= dist
            self.image = tegelane_pilt_v
        if klahv[pygame.K_d] or klahv[pygame.K_RIGHT]:
            self.x += dist
            self.image = tegelane_pilt
        if klahv[pygame.K_w] or klahv[pygame.K_UP]:
            self.y -= dist
        if klahv[pygame.K_s] or klahv[pygame.K_DOWN]:
            self.y += dist
    
    def HP_counter():
        font = pygame.font.SysFont(None, 30)
        tekst = font.render(str(HP), 1, eluvarv)
        tekst_rect = tekst.get_rect()
        tekst_rect.center = (TegelaneX, (TegelaneY-20))
        screen.blit(tekst,tekst_rect)


tegelane = Tegelane()


  #lisab spritei gruppi      
tegelane_grupp = pygame.sprite.Group()
tegelane_grupp.add(Tegelane())
sammud = 10
null = 0

#Damage checker#
moogard = Quest1()
if moogard == True:
    dmg = 10
else:
    dmg = 5

running = True
while running:
    
        #joonistab tausta
    screen.blit(taust1, [0,0])
        #joonistab tegelase
    tegelane.joonista(screen)
            #liikumine
    tegelane.liikumine()    
    Quest1()
    pygame.display.update()
    

    
    
    #ristist kinni panemine
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
    #hiire koordinaadi checkimine (delete later)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hiireX, hiireY = pygame.mouse.get_pos()
            print(hiireX, hiireY)
            

            
            possa_elu = fight(dmg, possa_elu)
            Elud = str(possa_elu) +", "+ str(HP)
            msgbox(Elud)

    pygame.display.flip()
    pygame.display.update()
            

        
     
        
            

