package sisteleitor;

public class Eleitor extends Pessoa{
	
	public boolean autorizado;
	public boolean realizado=false;
	
	public boolean ver_autorizado() {
		if (autorizado) {
			return true;
		}
		else {
			return false;	}
	}
	public void votar_e(Candidato c) {
      this.realizado=true;
	  c.somar_votos(); 	
	}
	
	public Eleitor(String n, String c) {
		super.nome=n;
		super.cpf=c;
	}
	
	public Eleitor() {
	}
}