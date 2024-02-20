from pyautogui import locateCenterOnScreen,click,locateOnScreen
from time import sleep
from pathlib import Path
from os.path import join,exists

ROOT = Path.cwd()
IMAGES = join(ROOT,"images","lol")

def observador()-> bool:
    """
    Detecta se a fila do League of Legends foi encontrada.
    """
    localizador = join(IMAGES,"ENCONTRADA.png")
    achei = False
    while not achei:
        try:
            print('procurando fila')
            if locateOnScreen(localizador,confidence=0.5):
                print('Fila encontrada')
                achei = True
                sleep(3)
        except:
            pass
            print('Aguardando')
            sleep(3)
        else:
            continue
    
    return achei


def aceitar_fila():
    clica = join(IMAGES,"ACEITAR.png")
    aceitar = locateCenterOnScreen(clica,confidence=0.3)
    click(aceitar.x,aceitar.y)
    sleep(4)


def bot():
    na_fila = join(IMAGES,'NA_FILA.png')
    if observador():
        aceitar_fila()
        sleep(10)
        if locateOnScreen(na_fila,confidence=0.4):
            return observador()
    



if __name__== "__main__":
    bot()
