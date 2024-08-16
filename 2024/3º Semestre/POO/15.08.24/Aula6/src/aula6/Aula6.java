package aula6;
import java.util.Scanner;
/**
 * @author antthLuca
 */
public class Aula6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        Pessoa john = new Pessoa("John", "4499999-9999", "R. Teste, 106, Jd. Krai");
        john.comprar();
        john.ativar_pessoa();
        john.comprar();
    }
}
