#include <stdio.h>
#include <locale.h>

int numMaior = 0;

int maiorNum(int *numMaior, int n) {
	setlocale(LC_ALL, "");
	
	if (*numMaior == 0) {
		*numMaior = n;
	} else if (n > *numMaior) {
		*numMaior = n;
	}
}

int main() {
	setlocale(LC_ALL, "");
	int x;
	
	for (int c = 1; c <= 3; c++) {
		printf("Digite um número inteiro:\n> ");
		scanf("%i", &x);
		
		maiorNum(&numMaior, x);
		
		printf("O maior número digitado é %i", numMaior);
	}
}
