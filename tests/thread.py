import threading
from time import sleep

def thread1():
    for i in range(0,10,1):
        print("\nThread1 executando...")
    
def thread2():
    for i in range(0,10,1):
        print("\nThread2 executando...")

# Criando e iniciando a thread
thread1 = threading.Thread(target=thread1).start()
thread2 = threading.Thread(target=thread2).start()


print("\nThread finalizada.\n")
