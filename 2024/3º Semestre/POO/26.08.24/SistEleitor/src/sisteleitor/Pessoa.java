package sisteleitor;

public class Pessoa {
	public String nome;
	public String cpf;
	public String data_nasc;
	public String cidade;
	public String uf;
	
	public void apresentar_pessoa() {
		System.out.println(nome+" "+cpf);
	}
	
	public boolean validar_cpf(String cpf){
		System.out.println("cpf é: "+cpf);
		// Remover pontuações do CPF (caso esteja com pontos e hífen)

		// Verificar se tem 11 dígitos
		if (cpf.length() != 11) {				    
			return false;
		
		}

		// Verificar se todos os dígitos são iguais (CPF inválido)
		if (cpf.equals(cpf.substring(0, 1).repeat(11))) {
		return false;
		}

		// Validar primeiro dígito verificador
		int soma = 0;
		for (int i = 0; i < 9; i++) {
		soma += Character.getNumericValue(cpf.charAt(i)) * (10 - i);
		}
		int digito1 = 11 - (soma % 11);
		if (digito1 >= 10) {
		digito1 = 0;
		}
		if (digito1 != Character.getNumericValue(cpf.charAt(9))) {
		return false;
		}

		// Validar segundo dígito verificador
		soma = 0;
		for (int i = 0; i < 10; i++) {
		soma += Character.getNumericValue(cpf.charAt(i)) * (11 - i);
		}
		int digito2 = 11 - (soma % 11);
		if (digito2 >= 10) {
		digito2 = 0;
		}
		if (digito2 != Character.getNumericValue(cpf.charAt(10))) {
		return false;
		}

		return true;
	}
}