package uninter.Moedas;

public abstract class Moeda {
	public double valor;
	
	 Moeda(double valor) {
		 this.valor = valor;
	}
	
	public abstract void getInfo();
	public abstract double converter();
	public abstract String tipoMoeda();
}
