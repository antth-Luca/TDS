#include <stdio.h>

const char* impar_par(int num) {
    if (num % 2 == 0) {
        return "par";
    } else {
        return "impar";
    }
}

int main() {
    int num;

    for (int c = 0; c < 10; c++) {
        printf("\nDigite o %i numero inteiro e positivo: ", c + 1);
        scanf("%i", &num);
        printf("O %i numero digitado, de valor %i, e %s!\n", c + 1, num, impar_par(num));
    }
}

