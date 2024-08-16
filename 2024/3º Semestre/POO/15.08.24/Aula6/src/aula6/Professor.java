package aula6;
/**
 * @author antthLuca
 */
public class Professor extends Pessoa {
    double salario;
    String disciplina;

    public Professor(String nome, int idade, char sexo, String email, String telefone, String endereço, double salario, String disciplina) {
        super(nome, idade, sexo, email, telefone, endereço);
        this.salario = salario;
        this.disciplina = disciplina;
    }
}
