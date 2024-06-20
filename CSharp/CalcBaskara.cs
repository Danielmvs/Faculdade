using System;


namespace Baskara

{
    class CalculoDeBaskara
     {
        static void Main()
        {
            

                Console.WriteLine("----------Calculo da Formula de Baskara----------");
                Console.WriteLine("");
                Console.WriteLine("Digite os coeficientes da equação ax^2 + bx + c = 0:");

                // O While vai testar o valor inserido pelo o usuário.
                // Enquanto o usuário digitar um valor errado o loop vai continuar, onde tambem "A" não pode ser igual 0
                // Quando o usuário digitar um valor certo o bloco while vai ser verdadeiro porem usando a " ! " faz a condiçao se torna false e sai do loop
                // o Console.Write é utilizado para o cursor continuar na mesma linha.
                // """este bloco de codigo se repete no coeficiente B e C"""""

                #region CoeficienteA

                Console.Write("a: ");
                double a;
                while (!double.TryParse(Console.ReadLine(), out a) || a == 0)
                {
                    Console.WriteLine("Por favor, digite um valor numérico não nulo para 'a':");
                }
                #endregion


                #region CoeficienteB

                Console.Write("b: ");
                double b;
                while (!double.TryParse(Console.ReadLine(), out b))
                {
                    Console.WriteLine("Por favor, digite um valor numérico para 'b':");
                }
                #endregion


                #region CoeficienteC

                Console.Write("c: ");
                double c;
                while (!double.TryParse(Console.ReadLine(), out c))
                {
                    Console.WriteLine("Por favor, digite um valor numérico para 'c':");
                }
                #endregion

                // bloco resposável por fazer todo o calculo representando as condições, onde delta pode ser: menor, igual ou maior que 0;
                #region CalculoDaRaiz

                double delta = (b * b) - 4 * a * c;

                if (delta < 0)
                {
                    Console.WriteLine("A equação não possui raízes reais.");
                    Console.Write("aparte qualquer tecla para sair:");
                    Console.ReadKey();

                }
                else if (delta == 0)
                {
                    double raiz = -b / (2 * a);
                    Console.WriteLine($"A equação possui uma raiz real:{raiz}");
                    Console.Write("aparte qualquer tecla para sair:");
                    Console.ReadKey();
                }
                else
                {
                    double raiz1 = (-b + Math.Sqrt(delta)) / (2 * a);
                    double raiz2 = (-b - Math.Sqrt(delta)) / (2 * a);
                    Console.WriteLine($"A equação possui duas raízes reais:{raiz1}, {raiz2}");
                    Console.Write("aparte qualquer tecla para sair:");
                    Console.ReadKey();
                }
                #endregion
            
        }
     }
}