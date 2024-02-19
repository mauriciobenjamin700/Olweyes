from pyautogui import locateCenterOnScreen,click,locateOnScreen
from time import sleep
from pathlib import Path


def observador(monitorar:bool=True)-> bool:
    """
    Detecta se a fila do League of Legends foi encontrada.
    """
    achei = False
    while monitorar:
        locateOnScreen('ENCONTRADA.png',confidence=0.7)
        print('Fila encontrada')
        monitorar = False
        achei = True
        print('Fila ainda não encontrada')
        sleep(5)
    
    return achei


def aceitar_fila():
    aceitar = locateCenterOnScreen('ACEITAR.png',confidence=0.5)
    click(aceitar.x,aceitar.y)
    sleep(8)

