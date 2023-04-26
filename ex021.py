# Faça um programa em python que abra
# e reproduza o áudio de arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load(ex021)
pygame.mixer.music.play()
pygame.event.wait()
