#include <stdio.h>

void impressora(char* palavra) {
	for (int c = 0; c < 50; c++) {
		printf("\n%s", palavra);
	}
}

int main() {
	char p[55];
	
	printf("Digite uma palavra: ");
	scanf("%s", &p);
	
	impressora(p);
}
