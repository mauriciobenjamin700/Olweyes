from threading import Thread
import time

# Variável de controle para interrupção das threads
stop_threads = False

def thread1():
    global stop_threads
    while not stop_threads:
        print("\nThread1 executando...")
        time.sleep(1)

def thread2():
    global stop_threads
    while not stop_threads:
        print("\nThread2 executando...")
        time.sleep(2)

# Criando e iniciando as threads
thread1 = Thread(target=thread1)
thread2 = Thread(target=thread2)

thread1.start()
thread2.start()

# Aguarda uma entrada do teclado para interromper as threads
print("Pressione Enter para interromper as threads...")
input()  # Aguarda a entrada do usuário

# Atualiza a variável de controle para interromper as threads
stop_threads = True

# Aguarda até que as threads terminem
thread1.join()
thread2.join()

print("\nThreads finalizadas.")
