from math import ceil
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
import funcoes
import pygame
import fim


def jogo(fator_dificuldade):
    pygame.init()
    clock = pygame.time.Clock()
    janela_j = Window(1280,720)

    #variaveis 
    lista_tiro = []
    delay = 0
    num_matriz = 0
    lista_alien = []
    vel = 150
    over = False
    num_linha = 3
    num_coluna = 8
    pontuacao = 0
    num_kills = 0
    lista_tiro_alien = []
    contador_tiro = 0
    vida = 3
    contador_invencibilidade = 0
    velx = 400
    vely = 600
    clock = pygame.time.Clock()

    #sprites
    nave = Sprite("assets\opa.png")
    background = Sprite("assets\Backgroundo.jpg")
    nave.set_position(1280/2 - nave.width ,600)
    nave_morrendo = Sprite("assets\opa_animacao.png", 4)
    nave_morrendo.set_total_duration(1000)
    #Usuario
    teclado = Window.get_keyboard()
    click = Window.get_mouse()  


    while True:
        clock.tick(60)
        background.draw()
        janela_j.draw_text(str(pontuacao), 100, 650, size=16, color=(0,255,0), font_name="Arial")

        if teclado.key_pressed("LEFT") and nave.x >= 0:
            nave.x -= velx * janela_j.delta_time()
        elif teclado.key_pressed("RIGHT") and nave.x <= 1280 - nave.width:
            nave.x += velx * janela_j.delta_time()

        delay = funcoes.piupiu(nave, background, janela_j, teclado, velx , vely, lista_tiro, delay)
        num_matriz, num_kills = funcoes.allien(lista_alien, num_matriz, num_linha, num_coluna, lista_alien, num_kills)
        vel, over = funcoes.movimento_alien(lista_alien, janela_j, vel, nave, over,  num_coluna, num_linha, fator_dificuldade) 
        pontuacao, num_kills, fator_dificuldade = funcoes.matar(lista_alien, lista_tiro, pontuacao, num_kills, fator_dificuldade)
        contador_tiro, vida, contador_invencibilidade, nave = funcoes.tiro_alien(lista_alien, lista_tiro_alien, contador_tiro, nave, vida, contador_invencibilidade, janela_j)


        if contador_invencibilidade > 0:
            nave_morrendo.x = nave.x
            nave_morrendo.y = nave.y
            nave_morrendo.draw()
            nave_morrendo.update()
            contador_invencibilidade -= 1
        else:
            nave.draw()

            
        if over:
            name = input("Insert your name: ")
            #Pontuação
            ranking_r = open('ranking.txt', 'r')
            conteudo = ranking_r.readlines()
            conteudo.append(name + " - " + str(pontuacao) + ".")
            ranking_r.close() 
            ranking_w = open('ranking.txt', 'w')
            ranking_w.writelines(conteudo)
            ranking_w.close()
            fim.acabou()  
            
        janela_j.update()
