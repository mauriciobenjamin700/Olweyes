from pyautogui import locateCenterOnScreen,click,locateOnScreen
from time import sleep
from os.path import join
import os

ROOT = os.getcwd()
IMAGES = join(ROOT,"images","lol")

ligado = False

def observar()-> bool:
    """
    Detecta se a fila do League of Legends foi encontrada.
    """
    localizador = join(IMAGES,"ENCONTRADA.png")
    global ligado
    achei = False
    
    try:
        if locateOnScreen(localizador,confidence=0.5):
            achei = True
    except:
        pass
    
    return achei


def aceitar_fila()-> bool:
    aceitei = False
    try:
        clica = join(IMAGES,"ACEITAR.png")
        aceitar = locateCenterOnScreen(clica,confidence=0.3)
        click(aceitar.x,aceitar.y)
        aceitar = True
    except:
        pass

    return aceitei

def hereges()-> bool:
    preciso_continuar_de_olho = False
    
    try:
        na_fila = join(IMAGES,'NA_FILA.png')
        if locateOnScreen(na_fila,confidence=0.4):
            preciso_continuar_de_olho = True
            
    except:
        pass
    
    return preciso_continuar_de_olho

if __name__== "__main__":
    pass
