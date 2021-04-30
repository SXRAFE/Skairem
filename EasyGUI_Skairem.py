import pygame
import sys
from easygui import *

valikud = ["sinine", "roheline", "punane",]

#Sassi EasyGUI koodijupp
#EasyGUI tegelase valimise interface + Juhend mängu jaoks -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
                return tegelane_pilt, tegelane_pilt_v
            
                i = 0
            else:
                i = 1
        elif Varv == "sinine":
            pilt2 = "Pildid/Ruutlid/Smol_sinine.png"
            jatka = ccbox('Oled kindel? ', 'Kontroll', image = pilt2) #Näitab previewd karakterist
            if jatka: #Kas oldi valmis alustama
               tegelane_pilt = pygame.image.load("Pildid/Ruutlid/Smol_sinine_MOOKNT.png").convert_alpha() #sätib ülejäänud mänguks värvi
               tegelane_pilt_v = pygame.image.load("Pildid/Ruutlid/Smol_sinine_MOOKNT_V.png").convert_alpha()
               return tegelane_pilt, tegelane_pilt_v
               i = 0
            else:
                i = 1
        elif Varv == "punane":
            pilt2 = "Pildid/Ruutlid/Smol_punane.png" 
            jatka = ccbox('Oled kindel? ', 'Kontroll', image = pilt2) #Näitab previewd karakterist
            if jatka: #Kas oldi valmis alustama
                tegelane_pilt = pygame.image.load("Pildid/Ruutlid/Smol_punane_MOOKNT.png").convert_alpha() #sätib ülejäänud mänguks värvi
                tegelane_pilt_v = pygame.image.load("Pildid/Ruutlid/Smol_punane_MOOKNT_V.png").convert_alpha()
                return tegelane_pilt, tegelane_pilt_v
                i = 0
            else:
                i = 1




def TUTORIAL(): #Seletab reegleid messageboxis
    msgbox("""
                                TERE TULEMAST!

                           KONTROLLID: WASD / ← ↑ → ↓
                           
                    INTERACTIMISEKS KÕNNI SPRITE'ILE OTSA
                    
                               EDU SEIKLUSEL!""")
#EasyGUI osa lõpp -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------