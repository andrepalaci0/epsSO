#include <stdio.h>
#include <pthread.h>
#include <stdatomic.h>
#include "error.h"

#define N 2 // Define o número desejado de iterações

atomic_int vez = 0; // Variável atômica para sincronização

void* processo_P0(void* arg) {
    for (int i = 0; i < N; ++i) {
        printf("P0: iteração %d\n", i);
        // Seção não crítica P0
        printf("Processo P0 executando seção não crítica\n");

        while (atomic_load(&vez) != 0);

        // Seção crítica P0
        printf("Processo P0 entrando na seção crítica\n");
        // Simulação de atividades na seção crítica
        printf("Processo P0 saindo da seção crítica\n");
        atomic_store(&vez, 1);
    }

    return NULL;
}

void* processo_P1(void* arg) {
    for (int i = 0; i < N; ++i) {
        printf("P1: iteração %d\n", i);
        // Seção não crítica P1
        printf("Processo P1 executando seção não crítica\n");

        while (atomic_load(&vez) != 1);

        // Seção crítica P1
        printf("Processo P1 entrando na seção crítica\n");
        // Simulação de atividades na seção crítica
        printf("Processo P1 saindo da seção crítica\n");
        atomic_store(&vez, 0);
    }

    return NULL;
}

int main() {
    pthread_t thread_P0, thread_P1;

    // Cria as threads para P0 e P1
    pthread_create(&thread_P0, NULL, processo_P0, NULL);
    pthread_create(&thread_P1, NULL, processo_P1, NULL);

    // Aguarda o término das threads
    pthread_join(thread_P0, NULL);
    pthread_join(thread_P1, NULL);

    return 0;
}
