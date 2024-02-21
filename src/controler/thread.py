import threading
from time import sleep

def minha_thread():
    print("Thread executando...")

# Criando e iniciando a thread
thread = threading.Thread(target=minha_thread)
thread.start()

# Esperando a thread terminar (opcional)
sleep(3)
thread.join()
thread.start()
sleep(3)
thread.join()


print("Thread finalizada.")
