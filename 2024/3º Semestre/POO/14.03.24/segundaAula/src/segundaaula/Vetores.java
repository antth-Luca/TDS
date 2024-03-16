package segundaaula;
import java.util.Scanner;
/*
 * @author ALUNO-0712
 */
public class Vetores {
    public static void main(String[] args) {
        String v[] = new String[5]; // Cria vetor já instanciando com 5 posições e de tipo String
        int i, n;
        Scanner tec = new Scanner(System.in);
        
        for(n = 0; n < v.length; n++) {
            System.out.println(String.format("Conteúdo para a posição %d: ", n));
            v[n] = tec.nextLine();
            System.out.println("");
        }
        
        System.out.println("-----------------------------");
        
        for(i = 0; i < v.length; i++) {
            System.out.println(String.format("Estou na posição %d, conteúdo: %s", i, v[i]));
        }
        
        System.out.println("\nACABOU!!!");
    }
}
