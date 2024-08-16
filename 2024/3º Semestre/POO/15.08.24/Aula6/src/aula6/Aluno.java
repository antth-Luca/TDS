package aula6;
/**
 * @author antthLuca
 */
public class Aluno extends Pessoa {
    String matricula;
    float nota;

    public Aluno(String nome, int idade, char sexo, String email, String telefone, String endereço, String matricula) {
        super(nome, idade, sexo, email, telefone, endereço);
        this.matricula = matricula;
        this.nota = 0;
    }
}
