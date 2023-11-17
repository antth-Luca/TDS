#include <stdio.h>

float media(int num1, int num2) {
	return (num1 + num2) / 2;
}

int main() {
	int n1, n2;
	
	printf("Digite um numero: ");
	scanf("%i", &n1);
	
	printf("Digite outro numero: ");
	scanf("%i", &n2);
	
	printf("A media entre %i e %i e de %.2f", n1, n2, media(n1, n2));
}
