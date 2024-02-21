from pyautogui import locateCenterOnScreen,click,locateOnScreen
from time import sleep
from os.path import join
import os

ROOT = os.getcwd()
IMAGES = join(ROOT,"images","lol")

achei = True

def observador(mode:int=3)-> bool:
    """
    Detecta se a fila do League of Legends foi encontrada.
    """
    localizador = join(IMAGES,"ENCONTRADA.png")
    achei = False
    while not achei:
        print("Estou de olho")
        try:
            if locateOnScreen(localizador,confidence=0.5):
                achei = True
                sleep(mode)
        except:
            sleep(mode)
        else:
            continue
    
    return achei


def aceitar_fila(mode:int=3):
    clica = join(IMAGES,"ACEITAR.png")
    aceitar = locateCenterOnScreen(clica,confidence=0.3)
    click(aceitar.x,aceitar.y)
    sleep(mode)


def bot(mode:int=3):
    na_fila = join(IMAGES,'NA_FILA.png')
    if observador(mode):
        aceitar_fila(mode)
        sleep(10)
        if locateOnScreen(na_fila,confidence=0.4):
            bot(mode)
    



if __name__== "__main__":
    bot()
