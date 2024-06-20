package uninter.Moedas;

public class Dolar extends Moeda{

	public Dolar(double valor) {
		super(valor);
	}

	@Override
	public void getInfo() {
		System.out.println("Dolar - " + valor);
	}

	@Override
	public double converter() {
		return valor *5;//O valor pode variar de acordo com a cotação atual
	}

	@Override
	public String tipoMoeda() {
		return "Dolar";
	}

}
