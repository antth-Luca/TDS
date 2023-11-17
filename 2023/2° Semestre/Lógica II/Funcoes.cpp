#include <stdio.h>
#include <math.h>

int soma(int a, int b) {
	int r;
	r = a + b;
	
	return r;
}

float jur_comp(float capital, float tx, int temp_aplic) {
	tx /= 100;
	float jc;
	jc = capital * pow((1 + tx), temp_aplic);
	
	return jc;
}

int main() {
	printf("Soma é %i\n", soma(2, 2));
	printf("R$ %.2f", jur_comp(1000, 5, 24));
}
