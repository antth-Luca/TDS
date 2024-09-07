package mercadinho;
/**
 * @antthLuca
 */
public class Cliente extends Pessoa {
    // Atributos da classe
    private int num_fidelidade;
    private int credito;

    // Construtor da classe, inicializando o crédito em 0
    public Cliente(int num_fidelidade, String nome, String cpf, String telefone) {
        super(nome, cpf, telefone); // Chama o construtor da classe Pessoa
        this.num_fidelidade = num_fidelidade;
        this.credito = 0;
    }

    // Método para adicionar 10 pontos de crédito
    public void gerarValores() {
        this.credito += 10;
    }

    // Getters para acessar os valores
    public int getNumFidelidade() {
        return num_fidelidade;
    }

    public int getCredito() {
        return credito;
    }
}
