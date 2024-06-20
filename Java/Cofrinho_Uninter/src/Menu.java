package uninter;

import java.util.Scanner;
import uninter.Moedas.*;

public class Menu {
	
	private Scanner scan; 
	
	public Menu() {
		scan = new Scanner(System.in);
	}
	
	public void mostrarMenuPricipal() {
		boolean controlador = true;
		while(controlador) {
			System.out.println("--------------------------------------------------- ");
			System.out.println("Olá Bem vindo ao Cofrinho");
			System.out.println("1 - Adcionar Moeda");
			System.out.println("2 - Remover Moeda");
			System.out.println("3 - Listar Moedas");
			System.out.println("4 - Calcular total valor convertido para real");
			System.out.println("0 - Encerrar");
			System.out.println("Escolha uma opção: ");
			int opcaoDoUsuario = scan.nextInt();
			System.out.println("--------------------------------------------------- ");
			
			switch(opcaoDoUsuario) {
			
				case 1:
					menuAdcionarMoeda();
					break;
				case 2:
					menuRemoverMoeda();
					break;
				case 3:
					Cofrinho.listarMoedas();
					break;
				case 4:
					Cofrinho.totalConvertido();
					break;	
				case 0: 
					controlador = false;
					System.out.println("Programa encerrado");
					break;
				default:
					System.out.println("--------------------------------------------------- ");
					System.out.println("Digite um Valor Válido");
					System.out.println("--------------------------------------------------- ");
			}
		}
	}
	public void menuAdcionarMoeda() {
		boolean controlador = true;
		while(controlador) {
			System.out.println("Escolha o tipo de moeda");
			System.out.println("1 - Real");
			System.out.println("2 - Dolar");
			System.out.println("3 - Euro");
			System.out.println("4 - Voltar");
			System.out.println(": ");
			int tipoMoeda = scan.nextInt();
			System.out.println("--------------------------------------------------- ");
			System.out.println("Digite o Valor Para Ser Adicionado:  ");
			double valorMoeda = scan.nextDouble();
			System.out.println("--------------------------------------------------- ");
			
			// e solicitado o tipo de moeda e valor que será adicionado, no qual sera criada uma instancia da moeda solicitada
			switch(tipoMoeda) {
				case 1:
					Cofrinho.Adicionar(new Real(valorMoeda));
					mostrarMenuPricipal();
					break;
				case 2:
					Cofrinho.Adicionar(new Dolar(valorMoeda));
					mostrarMenuPricipal();
					break;
				case 3:
					Cofrinho.Adicionar(new Euro(valorMoeda));
					mostrarMenuPricipal();
					break;
				case 4:
					mostrarMenuPricipal();
					break;
				default:
					System.out.println("--------------------------------------------------- ");
					System.out.println("Digite um Valor Válido");
					System.out.println("--------------------------------------------------- ");
			}
		}
	}
	
	public void menuRemoverMoeda() {
		boolean controlador = true;
		while(controlador) {
			System.out.println("Escolha o tipo de moeda para remover");
			System.out.println("1 - Real");
			System.out.println("2 - Dolar");
			System.out.println("3 - Euro");
			System.out.println("4 - Voltar");
			System.out.print(": ");
			int tipoMoeda = scan.nextInt();
			System.out.println("--------------------------------------------------- ");
			System.out.print("Digite o Valor Para Ser Removido:  ");
			double valorMoeda = scan.nextDouble();
			System.out.println("--------------------------------------------------- ");
			
			//é solicitado o tipo de moeda e o valor que o usuário vai retirar
			//sendo passado os valores para o método estático Remover
			switch(tipoMoeda) {
				case 1:
					Cofrinho.Remover(valorMoeda, "Real");
					mostrarMenuPricipal();
					break;
				case 2:
					Cofrinho.Remover(valorMoeda, "Dolar");
					mostrarMenuPricipal();
					break;
				case 3:
					Cofrinho.Remover(valorMoeda, "Euro");
					mostrarMenuPricipal();
					break;
				case 4:
					mostrarMenuPricipal();
					break;
				default:
					System.out.println("--------------------------------------------------- ");
					System.out.println("Digite um Valor Válido");
					System.out.println("--------------------------------------------------- ");
			}
		}
			
	}
	
}
