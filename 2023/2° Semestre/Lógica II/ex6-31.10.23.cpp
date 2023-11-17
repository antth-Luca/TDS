#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>

struct Aluno {
    char nome[55];
    int ra;
    float nota;
};

void append(struct Aluno **array, int *size, struct Aluno novoAluno) {
    (*size)++;
    *array = (struct Aluno *)realloc(*array, (*size) * sizeof(struct Aluno));

    if (*array) {
        (*array)[(*size) - 1] = novoAluno;
    } else {
        printf("Erro na alocação de memória.\n");
        exit(1);
    }
}

void opc1(struct Aluno **turma, int *totalAlunos) {
    if (*totalAlunos < 100) {
        struct Aluno novoAluno;

        printf("Qual o nome do aluno?\n> ");
        scanf("%s", novoAluno.nome);
        printf("\n");

        printf("Qual o RA do aluno %s?\n> ", novoAluno.nome);
        scanf("%d", &novoAluno.ra);
        printf("\n");

        printf("Qual a nota do aluno %s?\n> ", novoAluno.nome);
        scanf("%f", &novoAluno.nota);
        printf("\n");

        append(turma, totalAlunos, novoAluno);
        printf("Aluno inserido com sucesso!\n");
    } else {
        printf("A turma está cheia. Não é possível inserir mais alunos.\n");
    }
}

void opc2(struct Aluno *turma, int totalAlunos) {
    if (totalAlunos > 0) {
        printf("Lista de alunos:\n\n");

        for (int i = 0; i < totalAlunos; i++) {
            printf("Nome: %s\n", turma[i].nome);
            printf("RA: %d\n", turma[i].ra);
            printf("Nota: %.2f\n\n", turma[i].nota);
        }
    } else {
        printf("A turma está vazia. Nenhum aluno para listar.\n");
    }
}

int main() {
    setlocale(LC_ALL, "");

    struct Aluno *turma = NULL;
    int totalAlunos = 0;

    int opc;

    while (true) {
        printf("\n\n---------------------------\n"
			   "1 – Inserir\n"
               "2 – Listar\n"
               "3 – Sair\n"
               "> ");
        scanf("%d", &opc);
        printf("\n");

        switch (opc) {
            case 1:
                opc1(&turma, &totalAlunos);
                break;

            case 2:
                opc2(turma, totalAlunos);
                break;

            case 3:
                printf("Até mais...\n");
                free(turma);
                return 0;

            default:
                printf("Opção inválida!\n\n");
        }
    }

    return 0;
}

