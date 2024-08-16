package aula6;
/**
 * @author antthLuca
 */
public class Funcionario extends Pessoa {
    double salario;

    public Funcionario(String nome, int idade, char sexo, String email, String telefone, String endereço, double salario) {
        super(nome, idade, sexo, email, telefone, endereço);
        
        this.salario = salario;
    }
}
