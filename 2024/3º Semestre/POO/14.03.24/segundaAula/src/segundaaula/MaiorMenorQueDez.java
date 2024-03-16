package segundaaula;
import java.util.Scanner;
/*
 * @author ALUNO-0712
 */
public class MaiorMenorQueDez {
    public static void main(String[] args) {
        int opcao = 1;
        Scanner tec = new Scanner(System.in);
        
        while(opcao != 0) {
            System.out.print("Digite um valor: ");
            opcao = tec.nextInt();
            
            if(opcao < 10) {
                System.out.print("É menor que dez!");
            } else if(opcao > 10) {
                System.out.print("É maior que dez!");
            } else {
                System.out.print("O número é dez!");
            }
            System.out.println("\n");
        }
        
        System.out.println("SAIU!!!");
        tec.close();
    }
}
