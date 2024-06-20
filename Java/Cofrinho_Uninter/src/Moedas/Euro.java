package uninter.Moedas;

public class Euro extends Moeda{

	public Euro(double valor) {
		super(valor);
	}

	@Override
	public void getInfo() {
		System.out.println("Euro - " + valor);
	}

	@Override
	public double converter() {
		return valor *6;//O valor pode variar de acordo com a cotação atual
	}

	@Override
	public String tipoMoeda() {
		return "Euro";
	}

}
