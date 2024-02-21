from os.path import join
import os
#from threading import Thread

root = os.getcwd()
images = join(root, "images")


#VELOCIDADE DO BOT
TIME_SLOW = 10
TIME_NORMAL = 5
TIME_FAST = 3

#image = "images\\background\\0.jpg"
#image = "images\\background\\1.jpg"

IMAGE_OFF = join(images,"background","0.jpg")
IMAGE_ON = join(images,"background","1.jpg")


# TAMANHOS ORIGINAIS E FINAL
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# CONFIGS DOS BOTÕES DE LIGAR E DESLIGAR
MAIN_BUTTON_WIDTH = 200
MAIN_BUTTON_HEIGHT = 40

# CONFIG DOS BOTÕES DE PRECISÃO
PRECISION_BUTTON_WIDTH = MAIN_BUTTON_WIDTH//3
PRECISION_BUTTON_HEIGHT =  MAIN_BUTTON_HEIGHT//2

#COR DOS BOTÕES E DOS EFEITOS
BUTTON_COLOR = "#FAFF00"
OFF_BUTTON_COLOR = "#ABAE0C" 
HOVER_COLOR = "#00FF00"  # Cor quando o mouse passa sobre o botão
#OFF_BUTTON_COLOR = "#FF0000"

#estado da coruja e do bot, Inicia desligado, quando ligado recebe True
state = False
mode = 5
thread = None