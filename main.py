from math import ceil
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
import menu
import funcoes
import pygame
import fim


def jogo():
    pygame.init()
    clock = pygame.time.Clock()
    janela_j = Window(1280,720)

    #variaveis 
    lista_tiro = []
    delay = 0
    num_matriz = 0
    lista_alien = []
    vel = 1
    over = False
    num_linha = 3
    num_coluna = 8
    pontuacao = 0
    maior = 7
    menor = 0
    altura = 2
    maior_linha = 2
    menor_linha = 2
    maior_coluna = 0
    esquerda = 0
    direita = 0
    contador = 0


    #sprites
    nave = Sprite("assets\opa.png")
    background = Sprite("assets\Backgroundo.jpg")
    nave.set_position(1280/2 - nave.width ,600)

    #Usuario
    teclado = Window.get_keyboard()
    click = Window.get_mouse()  

    #variaveis
    velx = 300
    vely = 300

    while True:
        background.draw()
        nave.draw()
        fps = str(ceil(clock.get_fps()))

        janela_j.draw_text(str(pontuacao), 100, 650, size=16, color=(0,255,0), font_name="Arial")

        if teclado.key_pressed("LEFT") and nave.x >= 0:
            nave.x -= velx * janela_j.delta_time()
        elif teclado.key_pressed("RIGHT") and nave.x <= 1280 - nave.width:
            nave.x += velx * janela_j.delta_time()
        



        delay = funcoes.piupiu(nave, background, janela_j, teclado, velx , vely, lista_tiro, delay)
        num_matriz = funcoes.allien(lista_alien, num_matriz, num_linha, num_coluna, lista_alien)
        vel, over = funcoes.movimento_alien(lista_alien, janela_j, vel, nave, over,  num_coluna, num_linha) 
        pontuacao, maior, menor, maior_linha, menor_linha, maior_coluna, altura = funcoes.matar(lista_alien, lista_tiro, pontuacao, maior, menor, maior_linha, menor_linha, maior_coluna, altura)
     



        if teclado.key_pressed("ESC"):
            janela_j.close()

        clock.tick(60)
        janela_j.draw_text(fps, 20, 650, size=8, color=(0,0,255), font_name="Arial")

        janela_j.update()

        if over:
            fim.acabou()  