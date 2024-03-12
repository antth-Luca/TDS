package olamundo;
import java.util.Scanner;
/*
 * @author antthLuca
 */
public class OlaMundo {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Digite o ano de nascimento: ");
        int ano_nasc = (int) teclado.nextInt();
        int idade = (int) 2024 - ano_nasc;
        if (idade >= 18) {
            System.out.printf("%s anos é Maior de idade\n", idade);
        } else {
            System.out.printf("%s anos é Menor de idade\n", idade);
        }
    }
    
}