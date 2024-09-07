package mercadinho;

public class Mercadinho {
    public static void main(String[] args) {
        // Testando a classe Cliente
        Cliente cliente1 = new Cliente(12345, "João da Silva", "111.222.333-44", "(11) 91234-5678");
        System.out.println("== Cliente ==");
        System.out.println("Nome: " + cliente1.getNome());
        System.out.println("CPF: " + cliente1.getCpf());
        System.out.println("Telefone: " + cliente1.getTelefone());
        System.out.println("Número Fidelidade: " + cliente1.getNumFidelidade());
        System.out.println("Crédito Inicial: " + cliente1.getCredito());

        // Gerando valores para o cliente
        cliente1.gerarValores();
        System.out.println("Crédito após gerar valores: " + cliente1.getCredito());

        // Testando a classe Vendedor
        Vendedor vendedor1 = new Vendedor("Maria Souza", "987.654.321-00", "(21) 98888-8888", "MTR12345", 2500.00);
        System.out.println("\n== Vendedor ==");
        System.out.println("Nome: " + vendedor1.getNome());
        System.out.println("CPF: " + vendedor1.getCpf());
        System.out.println("Telefone: " + vendedor1.getTelefone());
        System.out.println("Matrícula: " + vendedor1.getMatricula());
        System.out.println("Salário: " + vendedor1.getSalario());
        System.out.println("Total de Vendas Inicial: " + vendedor1.getTotalVenda());
        System.out.println("Crédito Inicial: " + vendedor1.getCredito());

        // Gerando valores para o vendedor
        vendedor1.gerarValores();
        System.out.println("Crédito após gerar valores: " + vendedor1.getCredito());
    }
}
