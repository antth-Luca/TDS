package aula6;
/**
 * @author antthLuca
 */
public class Pessoa {
    String nome;
    int idade;
    char sexo;
    String email;
    String telefone;
    String endereço;
    boolean is_ativo;

    public Pessoa(String nome, int idade, char sexo, String email, String telefone, String endereço) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
        this.email = email;
        this.telefone = telefone;
        this.endereço = endereço;
        this.is_ativo = false;
    }
    
    public void ativar_pessoa() {
        this.is_ativo = true;
    }
    
    public void desativar_pessoa() {
        this.is_ativo = false;
    }
    
    public void comprar() {
        if (!this.is_ativo) {
            System.out.println("Compra não autorizada!");
        } else {
            System.out.println("Pessoa `" + this.nome + "` comprando...");
        }
    }
}
