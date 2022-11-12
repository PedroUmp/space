from PPlay.sprite import Sprite
import main
import funcoes 
from PPlay.window import *

def acabou():
    janela_game_over = Window(1280, 720)
    background = Sprite("assets\gameover.png")

    while True:
        background.draw()

        janela_game_over.update()