#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "");

    int eleitores, auxiliarVot, votosA = 0, votosB = 0, votosC = 0, votosD = 0, cont;
    char candA[50], candB[50], candC[50], candD[50];

    auxiliarVot = 0;
    strcpy(candA, "Zé ruela");
    strcpy(candB, "João Sem Braço");
    strcpy(candC, "Maria Trepadeira");
    strcpy(candD, "Chico Banana");

    printf("Quantos votantes teremos?\nR: ");
    scanf("%i", &eleitores);

    printf("_____Entrada do eleitor______\n");

    for (cont = 1; cont <= eleitores; cont++) {
        while (true) {
            printf("Eleitor %i, escolha em qual candidato você quer votar.\nTecle '[x] - para votar em candidato X'\n[1] - %s\n[2] - %s\n[3] - %s\n[4] - %s\n", cont, candA, candB, candC, candD);
            scanf("%i", &auxiliarVot);

            if (auxiliarVot != 1 && auxiliarVot != 2 && auxiliarVot != 3 && auxiliarVot != 4) {
                printf("\nOpção não identificada. Tente novamente!\n");
            } else {
                switch (auxiliarVot) {
                    case 1:
                        votosA++;
                        break;

                    case 2:
                        votosB++;
                        break;

                    case 3:
                        votosC++;
                        break;

                    case 4:
                        votosD++;
                        break;
                }
                break;
            }
        }
        printf("Voto confirmado para o candidato %i.\n", auxiliarVot);
        printf("\n_________Fim da sessão do Eleitor %i________\n\n", cont);
    }

    printf("_____Apuração dos votos______\n");
    printf("Resultado do primeiro turno:\n");
    printf("Candidato 1 (%s) teve %d votos\n", candA, votosA);
    printf("Candidato 2 (%s) teve %d votos\n", candB, votosB);
    printf("Candidato 3 (%s) teve %d votos\n", candC, votosC);
    printf("Candidato 4 (%s) teve %d votos\n", candD, votosD);

    float totalVotos = votosA + votosB + votosC + votosD;
    float porcentagemA = (votosA / totalVotos) * 100;
    float porcentagemB = (votosB / totalVotos) * 100;
    float porcentagemC = (votosC / totalVotos) * 100;
    float porcentagemD = (votosD / totalVotos) * 100;

    printf("Porcentagem de votos de cada candidato:\n");
    printf("Candidato 1 (%s): %.2f%%\n", candA, porcentagemA);
    printf("Candidato 2 (%s): %.2f%%\n", candB, porcentagemB);
    printf("Candidato 3 (%s): %.2f%%\n", candC, porcentagemC);
    printf("Candidato 4 (%s): %.2f%%\n", candD, porcentagemD);

    int maisVotado = votosA;
    int segundoMaisVotado = votosB;
    int candidato1 = 1, candidato2 = 2;

    if (votosB > maisVotado) {
        segundoMaisVotado = maisVotado;
        maisVotado = votosB;
        candidato1 = 2;
        candidato2 = 1;
    } else if (votosB > segundoMaisVotado) {
        segundoMaisVotado = votosB;
        candidato2 = 2;
    }

    if (votosC > maisVotado) {
        segundoMaisVotado = maisVotado;
        maisVotado = votosC;
        candidato1 = 3;
        candidato2 = 1;
    } else if (votosC > segundoMaisVotado) {
        segundoMaisVotado = votosC;
        candidato2 = 3;
    }

    if (votosD > maisVotado) {
        segundoMaisVotado = maisVotado;
        maisVotado = votosD;
        candidato1 = 4;
        candidato2 = 1;
    } else if (votosD > segundoMaisVotado) {
        segundoMaisVotado = votosD;
        candidato2 = 4;
    }

    printf("Resultado do segundo turno:\n");

    if (maisVotado > segundoMaisVotado) {
        printf("Candidato com mais votos é o vencedor!\n");
        printf("Parabéns ao Candidato ");
        if (maisVotado == votosA)
            printf("%s", candA);
        else if (maisVotado == votosB)
            printf("%s", candB);
        else if (maisVotado == votosC)
            printf("%s", candC);
        else if (maisVotado == votosD)
            printf("%s", candD);
        printf("\n");
    } else if (maisVotado == segundoMaisVotado) {
        printf("Empate no segundo turno. Realizando nova votação...\n");
        printf("Candidato 1 (%s) vs Candidato 2 (%s)\n", (candidato1 == 1) ? candA : ((candidato1 == 2) ? candB : ((candidato1 == 3) ? candC : candD)), 
                                                        (candidato2 == 1) ? candA : ((candidato2 == 2) ? candB : ((candidato2 == 3) ? candC : candD)));

        int votosCandidato1 = 0, votosCandidato2 = 0;

        for (cont = 1; cont <= eleitores; cont++) {
            while (true) {
                printf("Eleitor %i, escolha em qual candidato você quer votar no segundo turno.\nTecle '[x] - para votar em candidato X'\n[1] - Candidato 1\n[2] - Candidato 2\n", cont);
                scanf("%i", &auxiliarVot);

                if (auxiliarVot != 1 && auxiliarVot != 2) {
                    printf("\nOpção não identificada. Tente novamente!\n");
                } else {
                    if (auxiliarVot == 1) {
                        votosCandidato1++;
                        printf("Voto confirmado para o Candidato 1.\n");
                    } else {
                        votosCandidato2++;
                        printf("Voto confirmado para o Candidato 2.\n");
                    }
                    break;
                }
            }
            printf("\n_________Fim da sessão do Eleitor %i________\n\n", cont);
        }

        printf("Resultado da votação do segundo turno:\n");
        printf("Candidato 1 (%s) teve %d votos\n", (candidato1 == 1) ? candA : ((candidato1 == 2) ? candB : ((candidato1 == 3) ? candC : candD)), votosCandidato1);
        printf("Candidato 2 (%s) teve %d votos\n", (candidato2 == 1) ? candA : ((candidato2 == 2) ? candB : ((candidato2 == 3) ? candC : candD)), votosCandidato2);

        if (votosCandidato1 > votosCandidato2) {
            printf("Candidato 1 (%s) venceu o segundo turno!\n", (candidato1 == 1) ? candA : ((candidato1 == 2) ? candB : ((candidato1 == 3) ? candC : candD)));
        } else if (votosCandidato1 < votosCandidato2) {
            printf("Candidato 2 (%s) venceu o segundo turno!\n", (candidato2 == 1) ? candA : ((candidato2 == 2) ? candB : ((candidato2 == 3) ? candC : candD)));
        } else {
            printf("Empate no segundo turno. Não há um vencedor claro.\n");
        }
    } else {
        printf("Não houve um vencedor claro no primeiro turno. Será necessário um segundo turno.\n");
        printf("Os candidatos que irão para o segundo turno são:\n");
        printf("Candidato 1: %s\n", (candidato1 == 1) ? candA : ((candidato1 == 2) ? candB : ((candidato1 == 3) ? candC : candD)));
        printf("Candidato 2: %s\n", (candidato2 == 1) ? candA : ((candidato2 == 2) ? candB : ((candidato2 == 3) ? candC : candD)));
    }

    return 0;
}

