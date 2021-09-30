using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace Perceptron
{
    class RNA
    {

        static void Main(string[] args)
        {

             ///PerceptronTemplates.TrainNot();
             PerceptronTemplates.TrainNAND();
            
             double Salida = PerceptronTemplates.NAND(1,1,1);

             Console.WriteLine("\n OUT = " + Salida);
             Console.ReadKey();


        }


        }
    }

