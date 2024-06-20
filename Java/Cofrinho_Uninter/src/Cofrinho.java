package uninter;

import java.util.ArrayList;
import uninter.Moedas.*;

public class Cofrinho {
	
	private static ArrayList<Moeda> listaMoedas = new ArrayList<Moeda>();
	
	
	public static void Adicionar(Moeda moeda) {
		listaMoedas.add(moeda);
		System.out.println("valor: " + moeda.valor + " Adicionado com Sucerro ");
		System.out.println("--------------------------------------------------- ");
	}
	
	public static void Remover(double valor, String tipoMoeda) {
		boolean controlador = true; 
		for (int i = listaMoedas.size() - 1; i >= 0; i--) {
            Moeda moeda = listaMoedas.get(i);
            //se a moeda for do mesmo tipo existemte e o valor solicitado de retirada o valor será removido.
            if (moeda.tipoMoeda().equals(tipoMoeda) && moeda.valor == valor) {
                listaMoedas.remove(i);
                System.out.println("valor: " + moeda.valor + " removida com Sucerro ");
                controlador = false;
                break;
            }
		}
		if(controlador){
        	System.out.println("Não exite moeda com essa valor!!");
        }
		
	}
	public static void listarMoedas() {
		for (Moeda m : listaMoedas) {
			m.getInfo();
		}
		
		
	}
	//Percorre toda a lista e soma o valor convertido de cada moeda
	public static void totalConvertido() {
		double total = 0;
		for (int i = listaMoedas.size() - 1; i >= 0; i--) {
            Moeda moeda = listaMoedas.get(i);
            total += moeda.converter();
            }
		System.out.println("Total Convertido Em Real é: R$" + total);
		}
	
}
