package mercadinho;
/**
 * @antthLuca
 */
public class Vendedor extends Pessoa {
    // Atributos da classe Vendedor
    private String matricula;
    private double salario;
    private double totalVenda;
    private int credito;

    // Construtor da classe Vendedor
    public Vendedor(String nome, String cpf, String telefone, String matricula, double salario) {
        super(nome, cpf, telefone); // Chama o construtor da classe Pessoa
        this.matricula = matricula;
        this.salario = salario;
        this.totalVenda = 0.0;
        this.credito = 0; // Inicializa o crédito em 0
    }

    // Método para adicionar 2 pontos de crédito
    public void gerarValores() {
        this.credito += 2;
    }

    // Getters e Setters para acessar e modificar os atributos
    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public double getTotalVenda() {
        return totalVenda;
    }

    public void setTotalVenda(double totalVenda) {
        this.totalVenda = totalVenda;
    }

    public int getCredito() {
        return credito;
    }

    // Método principal para testar a classe
    public static void main(String[] args) {
        // Criação de um Vendedor com dados iniciais
        Vendedor vendedor = new Vendedor("Maria Souza", "987.654.321-00", "(21) 98888-8888", "MTR12345", 2500.00);

        // Exibindo as informações do vendedor
        System.out.println("Nome: " + vendedor.getNome());
        System.out.println("CPF: " + vendedor.getCpf());
        System.out.println("Telefone: " + vendedor.getTelefone());
        System.out.println("Matrícula: " + vendedor.getMatricula());
        System.out.println("Salário: " + vendedor.getSalario());
        System.out.println("Total de Vendas: " + vendedor.getTotalVenda());
        System.out.println("Crédito inicial: " + vendedor.getCredito());

        // Chamando o método gerarValores para adicionar 2 pontos de crédito
        vendedor.gerarValores();
        System.out.println("Crédito após gerar valores: " + vendedor.getCredito());
    }
}
