from PPlay.collision import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
import main
import fim
 

def piupiu(nave, background, janela, teclado, velx , vely, lista, delay):
    if teclado.key_pressed("UP") and delay == 0:
        criartiro(lista, nave)
        delay = 35
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





def criar_alien(lista, num_matriz, num_linha, num_coluna):
    if num_matriz == 0:
        for i in range(num_linha):
            linha =[]
            for j in range(num_coluna):
                    alien = Sprite("assets\Alien.png")
                    alien.x = 100 *(j+1)
                    alien.y = 50 *(i+1)
                    linha.append(alien)
            lista.append(linha)
        num_matriz += 1

    return num_matriz
            

def allien(lista, num_matriz, num_linha, num_coluna, lista_alien):
    criar_alien(lista, num_matriz, num_linha, num_coluna)
    for i, linha in enumerate(lista_alien):
        for j, alien, in enumerate(linha):
            lista[i][j].draw()



def movimento_alien(lista, janela, vel, nave, over, num_coluna, num_linha):
    colide = False
    for i, linha in enumerate(lista):
        for j, alien in enumerate(linha):
            lista[i][j].x += 3*vel
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



def matar(lista_alien, lista_tiro, pontuacao, maior, menor, maior_linha, menor_linha, maior_coluna, altura):
    for i, linha in enumerate(lista_alien):
        for j, alien in enumerate(linha):
            for k, tiro in enumerate(lista_tiro):
                if Collision.collided_perfect(tiro, alien) and tiro.x < lista_alien[maior_linha][maior].x and tiro.x > lista_alien[menor_linha][menor].x: #and tiro.y < lista_alien[maior_coluna][altura].y:
                    linha.remove(alien)
                    lista_tiro.remove(tiro)
                    pontuacao += 1
                    print("foi")
                    maior, menor, maior_linha, menor_linha, maior_coluna, altura = extremos(lista_alien, maior, menor, maior_linha, menor_linha, maior_coluna, altura)


    #print(maior)
    # print("maior ", maior)
    # print("maior_linha ", maior_linha)
    # print("\n")
    # print("menor ", menor)
    # print("menor_linha ", menor_linha)
    # print("\n")

    return pontuacao, maior, menor, maior_linha, menor_linha, maior_coluna, altura





def extremos(lista_alien, maior, menor, maior_linha, menor_linha, maior_coluna, altura):
    for i, linha in enumerate(lista_alien):
        for j, alien in enumerate(linha):
            if j <= menor:
                menor_linha = i
                menor = j
            if j >= maior:
                maior_linha = i
                maior = j

            if i <= altura:
                maior_coluna = j
                altura = i
    return maior, menor, maior_linha, menor_linha, maior_coluna, altura