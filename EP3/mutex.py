import threading

class CriticalSection:
    def __init__(self):
        self.mutex = threading.Lock()  # Criando o mutex

        self.shared_variable = 0  # Variável compartilhada

    def increment_shared_variable(self):
        for _ in range(5):
            self.mutex.acquire()  # Adquirindo o mutex para entrar na seção crítica
            self.shared_variable += 1  # Operação na variável compartilhada
            self.mutex.release()  # Liberando o mutex após a operação

    def run_threads(self):
        threads = []
        num_threads = 5

        # Criando threads
        for _ in range(num_threads):
            thread = threading.Thread(target=self.increment_shared_variable)
            threads.append(thread)

        # Iniciando as threads
        for thread in threads:
            thread.start()

        # Aguardando as threads finalizarem
        for thread in threads:
            thread.join()

        # Exibindo o valor final da variável compartilhada
        print(f"Valor final da variável compartilhada: {self.shared_variable}")

if __name__ == "__main__":
    cs = CriticalSection()
    cs.run_threads()
