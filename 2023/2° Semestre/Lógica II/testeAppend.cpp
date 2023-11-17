#include <stdio.h>
#include <stdlib.h>

void appendInt(int **array, int *size, int value) {
    (*size)++;
    *array = (int *)realloc(*array, (*size) * sizeof(int));

    if (*array) {
        (*array)[(*size) - 1] = value;
    } else {
        printf("Erro na alocação de memória.\n");
        exit(1);
    }
}

int main() {
    int *array = NULL;
    int size = 0;

    // Adiciona elementos ao array
    appendInt(&array, &size, 42);
    appendInt(&array, &size, 123);
    appendInt(&array, &size, 789);
    appendInt(&array, &size, 1000);

    // Imprime os elementos do array
    for (int i = 0; i < size; i++) {
        printf("%d\n", array[i]);
    }

    // Libera a memória alocada
    free(array);

    return 0;
}

