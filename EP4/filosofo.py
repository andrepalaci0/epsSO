from random import uniform
from time import sleep
from threading import Thread, Lock

plates = [0, 0, 0, 0, 0]  # 0 = Não comeu, 1 Já comeu


class Philosopher(Thread):
    execute = True  #variavel que define se é o momento de comer ou não

    def __init__(self, nome, left_hashi, right_hashi):  
        Thread.__init__(self)
        self.nome = nome
        self.left_hashi = left_hashi
        self.right_hashi = right_hashi

    def run(self):
        while self.execute:
            print(f"\n {self.nome} está pensando")
            sleep(uniform(0.5, 1))
            self.eat()

    def eat(self):
        """
        Pega o hashi 1 e tenta pegar o hashi 2. Se o hashi 2 estiver livre,
        o ele janta e solta os dois hashis em seguida,senão ele desiste de
        comer e continua pensando.
        """
        hashi1, hashi2 = self.left_hashi, self.right_hashi

        while self.execute:  # Enquanto a variavel 'execute' for true, tentará pegar os hashis para comer
            hashi1.acquire(True)  # tenta pegar o primeiro
            locked = hashi2.acquire(False)  # tenda adquirir o segundo hashi
            if locked:  #se conseguir (hashi disponivel), sai do loop de tentativa
                break 
            hashi1.release()  #se NÃO conseguir, solta o primeiro rashi
        else:
            return  #volta a pensar

        print(f"\n {self.nome} começou a comer")
        sleep(uniform(0.5, 1))
        print(f"\n {self.nome} terminou de comer")
        plates[names.index(self.nome)] += 1  
        print(" Quantas vezes cada filósofo comeu: ", plates) # quantidade de vezes que cada filósofo comeu
        hashi1.release()  # solta o hashi esquerdo
        hashi2.release()  # solta o hashi direito


names = ['Aristóteles', 'Platão', 'Sócrates', 'Pitágoras', 'Demócrito']  
hashis = [Lock() for _ in range(5)]
table = [Philosopher(names[i], hashis[i % 5], hashis[(i + 1) % 5]) for i in range(5)]
count = 0
print(f"Filósofos à mesa: {names}\n")
print(f"Estado atual da mesa: {plates}\n")
for _ in range(20): #O "range" define o total de vezes que cada filósofo ira tentar comer
    #portanto, o número total de execuções do programa é: range() x 5 (filosofos)
    Philosopher.execute = True  # Inicia a execução (ato de comer) de um determinado filósofo
    for philosopher in table: 
        try:
            count+= 1
            philosopher.start()  # inicia a thread respectiva do filósofo
            sleep(0.5) # aguarda 2 segundos para simular uma sincronização
        except RuntimeError:  # em caso de error da thread, pula a iteração
            pass
    sleep(uniform(0.5, 1))
    Philosopher.execute = False  # Finaliza a variável de execução do 
    
sleep(1)
print(f"Total de iterações: {count}")
