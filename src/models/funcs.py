from pyautogui import locateCenterOnScreen,click,locateOnScreen
from time import sleep
from pathlib import Path
from os.path import join

ROOT = Path.cwd()
IMAGES = join(ROOT,"images","lol")

def observador(monitorar:bool=True)-> bool:
    """
    Detecta se a fila do League of Legends foi encontrada.
    """
    achei = False
    target = join(IMAGES,"ENCONTRADA.png")
    
    while monitorar:
        locateOnScreen(target,confidence=0.7)
        print('Fila encontrada')
        monitorar = False
        achei = True
        print('Fila ainda não encontrada')
        sleep(5)
    
    return achei

def aceitar_fila():
    target = join(IMAGES,"ACEITAR.png")
    aceitar = locateCenterOnScreen(target,confidence=0.5)
    click(aceitar.x,aceitar.y)
    sleep(8)

