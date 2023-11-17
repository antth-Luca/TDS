#include <stdio.h>
#include <locale.h>

float salBruto, salLiq, descINSS = 0, descIRPF, deducao;

int main() {
	setlocale(LC_ALL, "");
	
	// Entrada de dados
	printf("\nQual o salário?\nR$ ");
	scanf("%f", &salBruto);
	
	
	// Cálculo INSS
	if (salBruto <= 1320) {
		descINSS += salBruto * 0.075;
	} else {
		descINSS += 99;
	}
	
	if (salBruto <= 2571.29) {
		descINSS += (salBruto - 1320) * 0.09;
	} else {
		descINSS += 112.61;
	}
	 
	if (salBruto <= 3856.94) {
		descINSS += (salBruto - 2571.29) * 0.12;
	} else {
		descINSS += 154.27;
	}
	 
	if (salBruto <= 7507.49) {
		descINSS += (salBruto - 3856.94) * 0.14;
	} else {
		descINSS += 511.07;
	}
	
	if (salBruto > 7507.49) {
		descINSS = 876.97;
	}
	
	// Cálculo IRPF
	salBruto -= descINSS;
	
	if (salBruto > 2112 && salBruto <= 2826.65) {
		descIRPF = (salBruto * 0.075) - 158.4;
	} else if (salBruto <= 3751.05) {
		descIRPF = (salBruto * 0.15) - 370.4;
	} else if (salBruto <= 4664.68) {
		descIRPF = (salBruto * 0.225) - 651.73;
	} else if (salBruto > 4664.68) {
		descIRPF = (salBruto * 0.275) - 884.96;
	}
	
	// Exibindo resultado
	printf("\n\nO salário de %.2f tem um desconto de INSS de %.2f e IRPF de %.2f. O salário líquido, final, é de %.2f!\n", salBruto + descINSS, descINSS, descIRPF, salBruto - descIRPF);
	printf("__________________________________________________________________________________________________\n");
}
