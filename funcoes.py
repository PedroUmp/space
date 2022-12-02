from PPlay.collision import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from random import randint
import main
import fim
 

def piupiu(nave, background, janela, teclado, velx , vely, lista, delay):
    if teclado.key_pressed("UP") and delay == 0:
        criartiro(lista, nave)
        delay = 50
    #tem tiro pra disparar
    if len(lista) > 0:
        for tiro in lista:
            tiro.draw()
            tiro.y -= vely * janela.delta_time()
            if tiro.y < -10:
                lista.remove(tiro)
    if delay > 0:
        delay -= 1
    return delay

def criartiro(lista, nave):
    tiro = Sprite("assets\Tiro.png")
    tiro.x = nave.x + 39
    tiro.y = nave.y - nave.height/2
    lista.append(tiro)





def criar_alien(lista, num_matriz, num_linha, num_coluna, num_kills):
    i = 1
    if num_matriz == 0 or num_kills == 24*i:
        num_kills = 0
        for i in range(num_linha):
            linha =[]
            for j in range(num_coluna):
                    alien = Sprite("assets\Alien.png")
                    alien.x = 100 *(j+1)
                    alien.y = 50 *(i+1)
                    linha.append(alien)
            lista.append(linha)
        num_matriz = 1
    i += 1

    return num_matriz, num_kills
            

def allien(lista, num_matriz, num_linha, num_coluna, lista_alien, num_kills):
    num_matriz, num_kills = criar_alien(lista, num_matriz, num_linha, num_coluna, num_kills)
    for i, linha in enumerate(lista_alien):
        for j, alien, in enumerate(linha):
            lista[i][j].draw()
    return num_matriz, num_kills

def criar_tiro_alien(lista_alien, lista_tiro_alien, contador_tiro):
    for i, linha in enumerate(lista_alien):
        for j, alien in enumerate(linha):

            if contador_tiro == 0:
                tiro_alien = Sprite("assets\Tiro.png")
                tiro_alien.x = lista_alien[i][j].x 
                tiro_alien.y =lista_alien[i][j].y
                lista_tiro_alien.append(tiro_alien)
                contador_tiro += 1
                return contador_tiro


def tiro_alien(lista_alien, lista_tiro_alien, contador_tiro, nave, vida, contador_ivencibilidade, janela):
   

    alien_atirando = randint(0,250)
    if alien_atirando == 10:
        contador_tiro = criar_tiro_alien(lista_alien, lista_tiro_alien, contador_tiro)
    if len(lista_tiro_alien):
        for tiro in lista_tiro_alien:
            tiro.draw()
            tiro.y += 600 * janela.delta_time()
            if Collision.collided_perfect(tiro, nave) and contador_ivencibilidade <= 0:
                contador_tiro = 0
                lista_tiro_alien.remove(tiro)
                vida -= 1
                nave.x = 640
                contador_ivencibilidade = 120
                return contador_tiro, vida, contador_ivencibilidade, nave
            elif tiro.y > 720:
                lista_tiro_alien.remove(tiro)
                contador_tiro = 0
                return contador_tiro, vida, contador_ivencibilidade, nave
            if vida == 0:
                fim.acabou()
    return contador_tiro, vida, contador_ivencibilidade, nave



def movimento_alien(lista, janela, vel, nave, over, num_coluna, num_linha, fator_dificuldade):
    colide = False
    for i, linha in enumerate(lista):
        for j, alien in enumerate(linha):
            lista[i][j].x += vel*fator_dificuldade * janela.delta_time() 
            if (lista[i][j].x >= janela.width - 50 or lista[i][j].x <= 0):
                colide = True
            if Collision.collided(lista[i][j], nave):
                over = True
    if colide == True:
        vel = vel*(-1)
        for i, linha in enumerate(lista):
            for j, alien in enumerate(linha):
                lista[i][j].y += 30
    
    return vel, over



# def matar(lista_alien, lista_tiro, pontuacao, esquerda, direita):
#     for i, linha in enumerate(lista_alien):
#         for j, alien in enumerate(linha):
#             for k, tiro in enumerate(lista_tiro):
#                 if Collision.collided_perfect(tiro, alien) and tiro.x > esquerda.x and tiro.x < direita.x:
#                     linha.remove(alien)
#                     lista_tiro.remove(tiro)
#                     pontuacao += 1

#     return pontuacao



def matar(lista_alien, lista_tiro, pontuacao, num_kills, fator_dificuldade):
    for i, linha in enumerate(lista_alien):
        for j, alien in enumerate(linha):
            for k, tiro in enumerate(lista_tiro):
                if Collision.collided_perfect(tiro, alien):
                    linha.remove(alien)
                    lista_tiro.remove(tiro)
                    pontuacao += 1
                    num_kills += 1
                    if num_kills == 24:
                        fator_dificuldade += 0.1
                        
    return pontuacao, num_kills, fator_dificuldade
                    
