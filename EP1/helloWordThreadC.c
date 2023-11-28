#include <stdio.h>
#include <pthread.h>
#include "error.h"


void* helloWorld(void* arg) {
    printf("Hello, world from thread!\n");
    return NULL;
}

int main() {
    printf("Hello, world from the main process!\n");

    int numThreads = 5; // Defina o número de threads que deseja criar
    pthread_t threads[numThreads];

    for (int i = 0; i < numThreads; i++) {
        if (pthread_create(&threads[i], NULL, helloWorld, NULL) != 0) {
            perror("pthread_create");
            return 1;
        }
    }

    for (int i = 0; i < numThreads; i++) {
        if (pthread_join(threads[i], NULL) != 0) {
            perror("pthread_join");
            return 1;
        }
    }

    return 0;
}
