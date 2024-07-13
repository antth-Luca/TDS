package aula4;
import java.util.Scanner;
/*
 * @author antthLuca
 */
public class Aula4 {
    public static void main(String[] args) {
        System.out.println("---------------------- INÍCIO! ---------------------");
        Scanner sc = new Scanner(System.in);

        Ex1(sc);
        Divisor();
        Ex2(sc);
        Divisor();
        Ex3(sc);
        Divisor();
        Ex4(sc);
        Divisor();
        Ex5(sc);
        Divisor();
        Ex6(sc);
        Divisor();
        Ex7(sc);
        Divisor();
        Ex8(sc);
        Divisor();
        Ex9(sc);
        Divisor();
        Ex10(sc);

        sc.close();
        System.out.println("----------------------- FIM! -----------------------");
    }
    

    public static void Divisor() {
        System.out.println("");
        System.out.println("----------------------------------------------------");
    }
    

    public static void Ex1(Scanner sc) {
        int num1;
        int num2;
        
        System.out.println("Exercício 1");

        System.out.print("Digite o primeiro número: ");
        num1 = sc.nextInt();
        
        System.out.print("Digite o segundo número: ");
        num2 = sc.nextInt();
        
        
        if (num1 == num2) {
            System.out.println("Os números são iguais!");
        } else {
            System.out.println("Os números são diferentes!");
        }
    }
    
    
    public static void Ex2(Scanner sc) {
        int a, b, c, d, e, max;

        System.out.println("Exercício 2");

        System.out.print("Digite o primeiro número: ");
        a = sc.nextInt();

        System.out.print("Digite o segundo número: ");
        b = sc.nextInt();

        System.out.print("Digite o terceiro número: ");
        c = sc.nextInt();

        System.out.print("Digite o quarto número: ");
        d = sc.nextInt();

        System.out.print("Digite o quinto número: ");
        e = sc.nextInt();

        max = Math.max(a, Math.max(b, Math.max(c, Math.max(d, e))));
        System.out.println("O maior número digitado é " + max);
    }
    
    
    public static void Ex3(Scanner sc) {
        System.out.println("Exercício 3");

        System.out.print("Digite a coordenada de 'x1': ");
        int x1 = sc.nextInt();

        System.out.print("Digite a coordenada de 'y1': ");
        int y1 = sc.nextInt();

        System.out.print("Digite a coordenada de 'x2': ");
        int x2 = sc.nextInt();

        System.out.print("Digite a coordenada de 'y2': ");
        int y2 = sc.nextInt();

        double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        System.out.println("A distência entre os pontos é de " + distance + " unidades!");
    }
    
    
    public static void Ex4(Scanner sc) {
        System.out.println("Exercício 4");

        System.out.print("Digite o salário do funcionário: R$ ");
        double sal = sc.nextDouble();

        double desc;
        int faixa = (int) (sal / 600);

        switch (faixa) {
            case 0: // salário <= 600.00
                desc = 0.0;
                break;
            case 1: // 600.00 < salário <= 1200.00
                desc = sal * 0.20;
                break;
            case 2: // 1200.00 < salário <= 2000.00
                desc = sal * 0.25;
                break;
            default: // salário > 2000.00
                desc = sal * 0.30;
                break;
        }

        System.out.println("O desconto é de R$ " + desc);
    }
    
    
    public static void Ex5(Scanner sc) {
        System.out.println("Exercício 5");

        int soma = 0;

        for (int c = 0; c <= 100; c++) {
            soma += c;

            System.out.print(c);
            if (c != 100) {
                System.out.print(" + ");
            } else {
                System.out.println(" = ");
            }
        }

        System.out.print(soma);
    }
    
    
    public static void Ex6(Scanner sc) {
        System.out.println("Exercício 6");
    }
    
    
    public static void Ex7(Scanner sc) {
        System.out.println("Exercício 7");
    }
    
    
    public static void Ex8(Scanner sc) {
        System.out.println("Exercício 8");
    }
    
    
    public static void Ex9(Scanner sc) {
        System.out.println("Exercício 9");
    }
    
    
    public static void Ex10(Scanner sc) {
        System.out.println("Exercício 10");
    }
}
