import threading

# Número de filósofos e garfos
NUM_FILOSOFOS = 5

# Lista de semáforos para representar os garfos
garfos = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]

# Função que representa a ação de pensar
def pensar(filosofo_id):
    print(f"Filósofo {filosofo_id} está pensando.")

# Função que representa a ação de comer
def comer(filosofo_id):
    print(f"Filósofo {filosofo_id} está comendo.")

# Função que simula a ação de um filósofo
def filosofo(filosofo_id):
    while True:
        pensar(filosofo_id)
        garfos[filosofo_id].acquire()  # Pega o garfo da esquerda
        garfos[(filosofo_id + 1) % NUM_FILOSOFOS].acquire()  # Pega o garfo da direita
        comer(filosofo_id)
        garfos[filosofo_id].release()  # Libera o garfo da esquerda
        garfos[(filosofo_id + 1) % NUM_FILOSOFOS].release()  # Libera o garfo da direita

# Cria uma thread para cada filósofo
filosofos = [threading.Thread(target=filosofo, args=(i,)) for i in range(NUM_FILOSOFOS)]

# Inicia as threads
for filosofo_thread in filosofos:
    filosofo_thread.start()

# Aguarda as threads terminarem
for filosofo_thread in filosofos:
    filosofo_thread.join()

