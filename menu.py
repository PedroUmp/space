from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
import dificuldade
import main

#janela 
janela = Window(1280, 720) 
janela.set_title("Space Invaders")
janela.set_background_color([8, 6, 42])

#sprites
botao_play = Sprite("assets\play.png")
botao_dificuldade = Sprite("assets\dificulty.png")
botao_sair = Sprite("assets\Back.png")

#posiçoes 
botao_play.set_position(janela.width/2 - botao_play.width/2, 250)
botao_dificuldade.set_position(janela.width/2 - botao_play.width/2, 350)
botao_sair.set_position(janela.width/2 - botao_sair.width/2, 450)

#Usuario
teclado = Window.get_keyboard()
click = Window.get_mouse()  


while True:
    janela.set_background_color([8, 6, 42])
    botao_play.draw()
    botao_dificuldade.draw()
    botao_sair.draw()
    janela.draw_text("Space Invaders", janela.width/2 - 310, 80, size=100, color=([255, 255, 255]), bold=False)



    #botoes
    if click.is_button_pressed(True) and click.is_over_object(botao_play):   
        main.jogo()

    if click.is_button_pressed(True) and click.is_over_object(botao_dificuldade):
        dificuldade.configuracoes()

    if click.is_button_pressed(True) and click.is_over_object(botao_sair):
        janela.close()

    if teclado.key_pressed("ESC"):
        janela.close()


    janela.update()