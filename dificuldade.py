from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
import menu



def configuracoes(): 
    #janela_d
    janela_d = Window(1280,720)
    janela_d.set_background_color([8, 6, 42])

    #sprites
    botao_easy = Sprite("assets\Facil.png")
    botao_medium = Sprite("assets\medio.png")
    botao_hard = Sprite("assets\dificil.png")
    botao_back2 = Sprite("assets\Back.png")


    botao_easy.set_position(janela_d.width/2 - botao_easy.width/2 - 545, 200)
    botao_medium.set_position(janela_d.width/2 - botao_medium.width/2 - 545, 300)
    botao_hard.set_position(janela_d.width/2 - botao_hard.width/2 - 545, 400)
    botao_back2.set_position(janela_d.width/2 - botao_back2.width/2 - 550, 650)

    #entradas
    teclado = Window.get_keyboard()
    click = Window.get_mouse() 


    while True:
        janela_d.draw_text("Dificuldade", janela_d.width/2 - 650, 80, size=100, color=([255, 255, 255]), bold=False)
        botao_easy.draw()
        botao_medium.draw()
        botao_hard.draw()
        botao_back2.draw()

        if click.is_button_pressed(True) and click.is_over_object(botao_back2):
            menu.inicio()
            
        janela_d.update()

