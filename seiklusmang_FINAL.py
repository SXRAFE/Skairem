import pygame
import sys
from easygui import *


pygame.init()

pygame.display.set_caption("Seiklusmäng")
screen = pygame.display.set_mode((960, 720))

#Sassi EasyGUI koodijupp
#EasyGUI tegelase valimise interface + Juhend mängu jaoks -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
taust1 =  pygame.image.load("Pildid/taustv1.jpg").convert_alpha()
mapi_list = []

valikud = ["sinine", "roheline", "punane",]
#funktsioon animatsiooni piltide laadimiseks
def animatsioonid(varv):
    animatsioon1 = pygame.image.load("Pildid/Ruutlid/animatsioonid/"+varv+"/ruutelparemjalg_parem.png")
    animatsioon2 = pygame.image.load("Pildid/Ruutlid/animatsioonid/"+varv+"/ruutelvasakjalg_parem.png")
    animatsioon1_v = pygame.image.load("Pildid/Ruutlid/animatsioonid/"+varv+"/ruutelparemjalg_vasak.png")
    animatsioon2_v = pygame.image.load("Pildid/Ruutlid/animatsioonid/"+varv+"/ruutelvasakjalg_vasak.png")
    return animatsioon1, animatsioon2, animatsioon1_v, animatsioon2_v

def mapi_pildid():
    number = 1
    for x in range(5):
        mapi_alamlist = []
        for y in range(5):           
            mapi_pilt = pygame.image.load("Pildid/Map/"+str(number)+".jpg")
            mapi_alamlist.append(mapi_pilt)
            number += 1
        mapi_list.append(mapi_alamlist)

def mapi_pildid_mask():
    print("tere")
    



        
        
        
    
    

def valivarv(): #Mängu käima pannes avaneb aken, kust saad valida oma kangelase värvi, see funktsioon võimaldab sellel juhtuda
    
    pilt = "Pildid/Ruutlid/Smol_roheline.png"
    i = 1
   
    while i == 1: #Loop juhuks, kui keegi ümber mõtleb ja tahab värvi vahetada
   
        Varv = buttonbox("Valige tegelase värv", "Tegelase valik", image = pilt, choices=valikud) #Värvivalikud
        if Varv is None:
            sys.exit(0) #Kui aken kinni panneks lõpetab programm töö

        if Varv == "roheline": 
            pilt2 = "Pildid/Ruutlid/Smol_roheline.png"
            jatka = ccbox('Oled kindel? ', 'Kontroll', image = pilt2) #Näitab previewd karakterist
            if jatka: #Kas oldi valmis alustama
                tegelane_pilt = pygame.image.load("Pildid/Ruutlid/Smol_roheline_MOOKNT.png").convert_alpha() #sätib ülejäänud mänguks värvi
                tegelane_pilt_v = pygame.image.load("Pildid/Ruutlid/Smol_roheline_MOOKNT_V.png").convert_alpha()
                varv = "roheline"

                return tegelane_pilt, tegelane_pilt_v, varv
            
                i = 0
            else:
                i = 1
        elif Varv == "sinine":
            pilt2 = "Pildid/Ruutlid/Smol_sinine.png"
            jatka = ccbox('Oled kindel? ', 'Kontroll', image = pilt2) #Näitab previewd karakterist
            if jatka: #Kas oldi valmis alustama
               tegelane_pilt = pygame.image.load("Pildid/Ruutlid/Smol_sinine_MOOKNT.png").convert_alpha() #sätib ülejäänud mänguks värvi
               tegelane_pilt_v = pygame.image.load("Pildid/Ruutlid/Smol_sinine_MOOKNT_V.png").convert_alpha()
               varv = "sinine"
               

               return tegelane_pilt, tegelane_pilt_v, varv
               i = 0
            else:
                i = 1
        elif Varv == "punane":
            pilt2 = "Pildid/Ruutlid/Smol_punane.png" 
            jatka = ccbox('Oled kindel? ', 'Kontroll', image = pilt2) #Näitab previewd karakterist
            if jatka: #Kas oldi valmis alustama
                tegelane_pilt = pygame.image.load("Pildid/Ruutlid/Smol_punane_MOOKNT.png").convert_alpha() #sätib ülejäänud mänguks värvi
                tegelane_pilt_v = pygame.image.load("Pildid/Ruutlid/Smol_punane_MOOKNT_V.png").convert_alpha()
                varv = "punane"

                return tegelane_pilt, tegelane_pilt_v, varv
                i = 0
            else:
                i = 1
    
def TUTORIAL(): #Seletab reegleid messageboxis
    msgbox("""
                                TERE TULEMAST!

                           KONTROLLID: WASD / ← ↑ → ↓
                           
                               MUUSIKA MUTE: M
                               
                             MUUSIAKA UNMUTE: N
                    
                               EDU SEIKLUSEL!""")

TUTORIAL()
tegelane_pildid = valivarv()
print(tegelane_pildid) #prindib tuple'i (delete later)

#EasyGUI osa lõpp -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

tegelane_pilt = pygame.transform.scale(tegelane_pildid[0], (64, 64))
tegelane_pilt_v = pygame.transform.scale(tegelane_pildid[1], (64, 64))
mapi_pildid() # loadib mapi pildid listi

#print(mapi_list)
#animatsioonid(tegelane_pildid[2])

def map(x, y):
    screen.blit(mapi_list[y][x], [0,0])
    
#tegelase class (välimus, liikumine, animatsioon(varsti))
class Tegelane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = tegelane_pilt
        self.rect = self.image.get_rect()
        
        self.x = 450
        self.y = 250
    
    def joonista(self, surface):
        surface.blit(self.image, (self.x, self.y), )
        
    def liikumine(self):
        klahv = pygame.key.get_pressed()
        dist = 0.2
        if klahv[pygame.K_a] or klahv[pygame.K_LEFT]:
            self.x -= dist
            self.image = tegelane_pilt_v
            #print(self.x)
            
        if klahv[pygame.K_d] or klahv[pygame.K_RIGHT]:
            self.x += dist
            self.image = tegelane_pilt
            #print(self.x)
            
        if klahv[pygame.K_w] or klahv[pygame.K_UP]:
            self.y -= dist
            #print(self.y)
            
            
        if klahv[pygame.K_s] or klahv[pygame.K_DOWN]:
            self.y += dist
            #print(self.y)
        

tegelane = Tegelane()
mapi_indeks_x = 2   
mapi_indeks_y = 2

majad1 = pygame.image.load("Pildid/Map/26_majad1.png").convert_alpha()
majad2 = pygame.image.load("Pildid/Map/26_majad2.png").convert_alpha()
  #lisab spritei gruppi      
tegelane_grupp = pygame.sprite.Group()
tegelane_grupp.add(Tegelane())
sammud = 10
null = 0




pygame.mixer.music.load("Muusika/BGmuss.wav")
pygame.mixer.music.play(-1)

kaib = True
kaib2 = True
running = True
heli = True

########################################### U NEED FOR HELISTUFF
heli = True
Hoon = pygame.image.load("Pildid/VolumYES.png").convert_alpha()
Hooff = pygame.image. load("Pildid/VolumNO.png").convert_alpha()
Hon = pygame.transform.scale(Hoon, [32,32])
Hoff = pygame.transform.scale(Hooff, [32,32])

helindus = Hon
###########################################
while running:
        #joonistab tausta

    map(mapi_indeks_x, mapi_indeks_y)
    
    if tegelane.x <= 0:         
        if mapi_indeks_x == 0:
            tegelane.x = 0
        else:
            #print("haha")
            mapi_indeks_x = mapi_indeks_x - 1
            tegelane.x = 890
     
    if tegelane.x >= 896: #960 - 64px (playeri mõõtmed 64x64)
        if mapi_indeks_x == 4:            
            tegelane.x = 896

        else:
            mapi_indeks_x += 1
            tegelane.x = 0

        
    if tegelane.y <= 0:
        if mapi_indeks_y == 0:
            tegelane.y = 0

        else:
            mapi_indeks_y -= 1
            tegelane.y = 710

        
    if tegelane.y >= 720:
        if mapi_indeks_y == 4:
            tegelane.y = 656 #720 - 64px (playeri mõõtmed 64x64
        else:
            mapi_indeks_y += 1
            tegelane.y = 10


    

        #joonistab tegelase
    tegelane.joonista(screen)
    if mapi_indeks_x == 0 and mapi_indeks_y == 0:
        screen.blit(majad1,[360, 322])
    if mapi_indeks_x == 1 and mapi_indeks_y == 1:
        screen.blit(majad2, [280, 340])
    
            #liikumine
    tegelane.liikumine()
    screen.blit(helindus, [7, 7]) #ALSO FOR HELISTUFF
        
# Mängib teatud ruudus teatud muusikat PLS COPY PASTE  CHANGED FEW TING
    if heli == True:
        if kaib == True:
            if mapi_indeks_x == 1 and mapi_indeks_y == 3:
                pygame.mixer.music.load("Muusika/Royal.wav")
                pygame.mixer.music.play(-1)
                kaib = False
                kaib2 = True
                helindus = Hon
        if kaib2 == True:
            if mapi_indeks_x != 1 or mapi_indeks_y != 3:
                pygame.mixer.music.load("Muusika/BGmuss.wav")
                pygame.mixer.music.play(-1)
                kaib2 = False
                kaib = True
                helindus = Hon

            
        
#--------------------------------------------------------------------    

    
    
    #ristist kinni panemine
    for event in pygame.event.get():       
        if event.type == pygame.QUIT:
            pygame.quit()
    #hiire koordinaadi checkimine (delete later)

################################ MUCH NEED SUCH WOW WOEK MUTE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                heli == False

                pygame.mixer.music.stop()
                helindus = Hoff
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                heli == True

                pygame.mixer.music.play(-1)
                helindus = Hon
#######################################################        
         
         
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hiirecord = pygame.mouse.get_pos()
            print(hiirecord)
            

                
                
            
            
        
    pygame.display.update()
            

        
     
        
            

