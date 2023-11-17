#include <stdio.h>
#include <ctype.h>
#include <locale.h>

int main() {
	int x=1, salas, elet, pessoas, m2, result;
	char sol;
	setlocale(LC_ALL, "");
	
	printf("Quantas salas terão seus BPU calculados? ");
	scanf("%i", &salas);
	for (x; x <= salas; x++) {
		printf("\nQuantos m² tem a %i° sala? ", x);
		scanf("%i", &m2);
		printf("\nA sala é exposta ao sol? ");
		scanf(" %c", &sol);  // Use espaço antes de %c para evitar problemas de buffer.
		while (toupper(sol) != 'S' && toupper(sol) != 'N') {
			printf("\nResposta errada! Tente novamente...");
			printf("\nA sala é exposta ao sol? ");
			scanf(" %c", &sol);
		}
		printf("\nQuantos equipamentos eletrônicos existem nesta sala? ");
		scanf("%i", &elet);
		printf("\nQuantas pessoas estarão usando esta sala? ");
		scanf("%i", &pessoas);
		if (toupper(sol) == 'S') {
			result = (800 * m2) + ((pessoas - 1) * 600) + (600 * elet);
			printf("\n\n------------------------");
			printf("\nSerão necessários %i BPUs para a %i° sala.", result, x);
			printf("\n------------------------\n\n");
		} else {
			result = (600 * m2) + ((pessoas - 1) * 600) + (600 * elet);
			printf("\n\n------------------------");
			printf("\nSerão necessários %i BPUs para a %i° sala.", result, x);
			printf("\n------------------------\n\n");
		}
	}
}

