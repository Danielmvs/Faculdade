package uninter.Moedas;

public class Real extends Moeda {
	
	public Real(double valor) {
		super(valor);
	}

	@Override
	public void getInfo() {
		System.out.println("Real - " + valor);
	}

	@Override
	public double converter() {
		return valor * 1;
	}

	@Override
	public String tipoMoeda() {
		return "Real";
	}
	
}
