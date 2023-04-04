#play music
#01option
import pygame #biblioteca de jogos e jogos tocam musica
print ('Playing music')
pygame.init()
pygame.mixer.music.load("ex01.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

#02option
from playsound import playsound
playsound('ex01.mp3')