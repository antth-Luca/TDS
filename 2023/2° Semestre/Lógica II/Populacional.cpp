#include <stdio.h>

main () {
	float eua = 338788000;
	float india = 1430000000;
	int ano = 2023;
	
	while (eua <= india) {
		eua += eua * (1.67 / 100);
		india += india * (0.61 / 100);
		ano++;
	}
	printf("Os EUA ultrapassaram a Índia em habitantes aproximadamente no ano de %i.\nConsiderando que as taxas sejam fixas!", ano);
}
