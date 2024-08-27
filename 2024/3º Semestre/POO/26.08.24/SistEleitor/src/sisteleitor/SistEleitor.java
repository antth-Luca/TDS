package sisteleitor;
/**
 * @antthLuca
 */
public class SistEleitor {
    public static void main(String[] args) {
        Eleitor luca = new Eleitor("Luca Antony","40350661090");
        Eleitor smurf = new Eleitor("Smurf da Silva","07823237903");
      
        Candidato candidato1 = new Candidato("Joaquim","00335264948");
        Candidato candidato2 = new Candidato("Wilson","52546975048");

        Eleitor[] eleit = new Eleitor[10];
        Candidato[] cand = new Candidato[10];
      
        eleit[0]=luca;
        eleit[1]=smurf;
      
        cand[0]=candidato1;
        cand[1]=candidato2;
      
        int i=0;
        while (i<2) {
            eleit[i].votar_e(candidato1); 
            i=i+1;
        }
     
        i=0;
        while (i<2) {
            System.out.println(cand[i].nome+" votos?:"+cand[i].votos); 
            i=i+1;
        }	
    }
}