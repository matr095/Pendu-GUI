__author__ = 'mathieurossetto'

import pygame
import random
pygame.init()
pygame.font.init()

def jouer():
    mot = random.randint(0,9)
    if mot == 0:
        mot = "voiture"

    if mot == 1:
        mot = "grandir"

    if mot == 3:
        mot = "penser"

    if mot == 4:
        mot = "jouer"

    if mot == 5:
        mot = "libre"

    if mot == 6:
        mot = "frite"

    if mot == 7:
        mot = "manger"

    if mot == 8:
        mot = "voile"

    if mot == 9:
        mot = "voler"

    print(mot)

    ###inistalisation de la fenetre
    fen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Pendu GUI by MatR")
    print(pygame.font.get_fonts)
    font = pygame.font.Font(None, 48)
    lettre = pygame.font.Font(None, 32)
    title = font.render("Pendu par MatR", True, (120,120,255))
    fen.blit(title, (10,10))
    pygame.display.update()


    ###boucle des evenements
    continuer = 1
    tentative = 11
    tentativeJuste = 0

    while continuer:
        for event in pygame.event.get():
            souris = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                continuer = 0
            if event.type == pygame.KEYDOWN:
                lettre = pygame.key.name(event.key)

                if lettre in mot:
                    print(lettre)
                    display = pygame.font.Font(None, 32)
                    disp = display.render(lettre, True, (170,170,255))
                    while tentativeJuste >= 0:
                        print(tentativeJuste)
                        fen.blit(disp, (20 + 20 * (mot.index(lettre)),50))
                        break
                    tentativeJuste += 20
                    pygame.display.update()

                    if tentativeJuste == len(mot) * 20:
                        gagne = display.render("Bravo! Tu es un champion... . Le mot est " + mot, True, (155,255,155))
                        fen.blit(gagne, (20,190))
                        pygame.display.update()


                if lettre not in mot:
                    print(lettre)
                    tentative -= 1
                    displayFaux = pygame.font.Font(None, 70)
                    dispTentative = displayFaux.render("__________________", True, (255,100,100))
                    fen.blit(dispTentative, (200 - (50 * tentative),130))
                    pygame.display.update()

                    if tentative <= 0:

                        display = pygame.font.Font(None, 32)
                        perdu = display.render("Gros Nul! Retourne jouer aux billes...", True, (255,0,0))

                        fen.blit(perdu, (20,150))
                        pygame.display.update()
                        if tentative <= -1:
                             jouer()



jouer()
