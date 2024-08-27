package sisteleitor;

public class Candidato extends Pessoa {
	public String cargo;
	public String partido;
	public int votos=0;
	public boolean apto;
	
	public void somar_votos(){
		votos=votos+1;
	}

	public Candidato(String n, String c) {
		super.nome=n;
		super.cpf=c;
	}
}
