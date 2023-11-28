import threading

# Variável global que simula a seção crítica
count = 0

# Mutex para garantir a exclusão mútua
mutex = threading.Semaphore(1)

# Função que representa a seção crítica
def secao_critica():
    global count
    count += 1

# Função executada por cada thread
def thread_func(thread_id):
    global count
    for _ in range(10):
        mutex.acquire()  # Bloqueia o acesso à seção crítica
        secao_critica()
        print(f"Thread {thread_id} entrou na seção crítica. Count = {count}")
        mutex.release()  # Libera o acesso à seção crítica

# Cria duas threads
thread1 = threading.Thread(target=thread_func, args=(1,))
thread2 = threading.Thread(target=thread_func, args=(2))

# Inicia as threads
thread1.start()
thread2.start()

# Aguarda as threads terminarem
thread1.join()
thread2.join()

print("Ambas as threads terminaram.")
