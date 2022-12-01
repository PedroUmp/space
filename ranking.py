from PPlay.window import *
from PPlay.gameimage import *
from pygame import mixer
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *


def translate(ranking):
    arquivo = open(ranking)
    pontuacao = []
    for elemento in arquivo:
        temp = elemento.split(".")         
        for i in temp:
            pontuacao.append(i)
    arquivo.close()
    return pontuacao

def rank():
    janela_largura = 1280
    janela_altura = 720

    janela = Window(janela_largura, janela_altura)
    janela.set_title("Menu")

    teclado = janela.get_keyboard()
    background = Sprite("assets\Backgroundo.jpg")

    lista = translate("ranking.txt")

    lista.reverse()

    while True:
        background.draw()
        limite = 0
        altura = 0
        janela.draw_text("Leaderboard:", janela_largura / 2 - 140 , 30 + altura, size= 50, color=(0, 100, 255), font_name="Arial", bold=True, italic=True)
        for i, conteudo in enumerate(lista):
            if i == 0:
                pass
            if limite <= 5:
                janela.draw_text(str(conteudo), janela_largura / 2 - 130 , 70 + altura, size=32, color=(0, 100, 255), font_name="Arial", bold=True, italic=False)
                limite += 1
                altura += 60
        if teclado.key_pressed("ESC"):
            break
        janela.update()
