package aula3;
/*
 * @author antthLuca
 */
public class Radio {
    private String marca;
    private double estacao;
    private int volume;

    public Radio(String marca, double estacao) {
        this.marca = marca;
        this.estacao = estacao;
        this.volume = 50;
    }

    public void getMarca() {
        System.out.println("Super qualidade. Minha marca é " + marca);
    }

    public void getEstacao() {
        if (estacao == 0) {
            System.out.println("Não estou ouvindo nada! Silêncio é o meu momento");
        } else {
            System.out.println("Estou escutando " + estacao);
        }
    }

    public void getVolume() {
        System.out.println("O volume atual é de " + volume);
    }
    
    public void aumentar_volume() {
        this.volume += 1;
    }
    
    public void diminuir_volume() {
        this.volume -= 1;
    }
}
