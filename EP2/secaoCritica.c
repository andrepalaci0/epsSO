#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define TRUE 1
#define N 2 // Defina o número de iterações desejado

int vez = 0; // Variável compartilhada
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER; // Mutex para sincronização

void* processo_P0(void* arg) {
    for (int i = 0; i < N; ++i) {
        printf("Iteração P0: %d\n", i);
        while (1) {
            pthread_mutex_lock(&mutex);
            if (vez == 0) {
                pthread_mutex_unlock(&mutex);
                break;
            }
            pthread_mutex_unlock(&mutex);
        }

        // Seção crítica P0
        printf("Processo P0 entrando na seção crítica\n");
        // Simulação de atividades na seção crítica
        printf("Processo P0 saindo da seção crítica\n");

        pthread_mutex_lock(&mutex);
        vez = 1;
        pthread_mutex_unlock(&mutex);

        // Seção não crítica P0
        printf("Processo P0 executando seção não crítica\n");
    }

    return NULL;
}

void* processo_P1(void* arg) {
    for (int i = 0; i < N; ++i) {
        printf("Iteração P1: %d\n", i);
        while (1) {
            pthread_mutex_lock(&mutex);
            if (vez == 1) {
                pthread_mutex_unlock(&mutex);
                break;
            }
            pthread_mutex_unlock(&mutex);
        }

        // Seção crítica P1
        printf("Processo P1 entrando na seção crítica\n");
        // Simulação de atividades na seção crítica
        printf("Processo P1 saindo da seção crítica\n");

        pthread_mutex_lock(&mutex);
        vez = 0;
        pthread_mutex_unlock(&mutex);

        // Seção não crítica P1
        printf("Processo P1 executando seção não crítica\n");
    }

    return NULL;
}

int main() {
    pthread_t thread_P0, thread_P1;

    // Criação das threads para P0 e P1
    pthread_create(&thread_P0, NULL, processo_P0, NULL);
    pthread_create(&thread_P1, NULL, processo_P1, NULL);

    // Aguarda o término das threads
    pthread_join(thread_P0, NULL);
    pthread_join(thread_P1, NULL);

    return 0;
}
