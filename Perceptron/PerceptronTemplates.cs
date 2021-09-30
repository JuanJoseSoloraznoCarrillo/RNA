using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;



namespace Perceptron
{
    class PerceptronTemplates
    {


        public static double w1, w2, w3, bias;
        public static bool   sw = false; //flag
        public static int    count;

        public static double W1;
        public static double W2;
        public static double W3;
        public static double BIAS;

        public static void TrainNAND()
        {
            PerceptronTemplates Neuro = new PerceptronTemplates();
            Random rand = new Random();

            while (!sw)
            {
                count = count + 1;
                sw = true; //flag

                w1 = rand.NextDouble() - rand.NextDouble();
                w2 = rand.NextDouble() - rand.NextDouble();
                w3 = rand.NextDouble() - rand.NextDouble();
                bias = rand.NextDouble() - rand.NextDouble();

                Console.WriteLine("\n-------------Epoch " + count + "------------------\n");
                Console.WriteLine("  w1: -------> " + w1);
                Console.WriteLine("  w2: -------> " + w2);
                Console.WriteLine("  w3: -------> " + w3);
                Console.WriteLine("  bias:------> " + bias);
                Console.Write(" \n In_1 = 1  In_2 = 1  In_3 = 1----> " + Neuro.Sigmoide(Neuro.NeuronNAND(1f, 1f, 1f, w1, w2, w3, bias)));
                Console.Write(" \n In_1 = 1  In_2 = 1  In_3 = 0----> " + Neuro.Sigmoide(Neuro.NeuronNAND(1f, 1f, 0f, w1, w2, w3, bias)));
                Console.Write(" \n In_1 = 1  In_2 = 0  In_3 = 1----> " + Neuro.Sigmoide(Neuro.NeuronNAND(1f, 0f, 1f, w1, w2, w3, bias)));
                Console.Write(" \n In_1 = 1  In_2 = 0  In_3 = 0----> " + Neuro.Sigmoide(Neuro.NeuronNAND(1f, 0f, 0f, w1, w2, w3, bias)));
                Console.Write(" \n In_1 = 0  In_2 = 1  In_3 = 1----> " + Neuro.Sigmoide(Neuro.NeuronNAND(0f, 1f, 1f, w1, w2, w3, bias)));
                Console.Write(" \n In_1 = 0  In_2 = 1  In_3 = 0----> " + Neuro.Sigmoide(Neuro.NeuronNAND(0f, 1f, 0f, w1, w2, w3, bias)));
                Console.Write(" \n In_1 = 0  In_2 = 0  In_3 = 1----> " + Neuro.Sigmoide(Neuro.NeuronNAND(0f, 0f, 1f, w1, w2, w3, bias)));
                Console.Write(" \n In_1 = 0  In_2 = 0  In_3 = 0----> " + Neuro.Sigmoide(Neuro.NeuronNAND(0f, 0f, 0f, w1, w2, w3, bias)));


                if (Neuro.Sigmoide(Neuro.NeuronNAND(1f, 1f, 1f, w1, w2, w3, bias)) != 0)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNAND(1f, 1f, 0f, w1, w2, w3, bias)) != 1)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNAND(1f, 0f, 1f, w1, w2, w3, bias)) != 1)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNAND(1f, 0f, 0f, w1, w2, w3, bias)) != 1)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNAND(0f, 1f, 1f, w1, w2, w3, bias)) != 1)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNAND(0f, 1f, 0f, w1, w2, w3, bias)) != 1)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNAND(0f, 0f, 1f, w1, w2, w3, bias)) != 1)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNAND(0f, 0f, 0f, w1, w2, w3, bias)) != 1)
                {
                    sw = false;
                }

                W1 = w1;
                W2 = w2;
                W3 = w3;
                BIAS = bias;
                Console.WriteLine("\n\n----------   Training.....   -----------");


            } //End While

            Console.WriteLine("Perceptron NAND is trained, Epoch = " + count);
      
            Console.ReadKey();

        }//End method train


        ////////////   PERCEPTRON NOT   //////////
        public static void TrainNot()
        {
            sw = false; //flag
            count = 0;

            PerceptronTemplates Neuro = new PerceptronTemplates();
            Random rand = new Random();

            //////////////  TRAINING  ////////////
            while (!sw)
            {
                count = count + 1;
                sw = true;

                w1   = rand.NextDouble() - rand.NextDouble();
                bias = rand.NextDouble() - rand.NextDouble();

                Console.WriteLine("\n-------------Epoch " + count + "------------------\n");
                Console.WriteLine("  w1:  ------->  " + w1);
                Console.WriteLine("  bias:------->  " + bias);
                Console.Write(" \n In_1 = 1  ---->  " + Neuro.Sigmoide(Neuro.NeuronNot(1f, w1, bias)));
                Console.Write(" \n In_1 = 0  ---->  " + Neuro.Sigmoide(Neuro.NeuronNot(0f, w1, bias)));


                if (Neuro.Sigmoide(Neuro.NeuronNot(0f, w1, bias)) != 1)
                {
                    sw = false;
                }

                if (Neuro.Sigmoide(Neuro.NeuronNot(1f, w1, bias)) != 0)
                {
                    sw = false;
                }

                Console.WriteLine("\n\n----------   Training.....   -----------");


            }//End while

            Console.WriteLine("Perceptron NOT is trained, Epoch = " + count);
            Console.ReadKey();

        }//End method TrainNot


        //////  Activaction Functions  /////
        public double Sigmoide(double a)
        {
            return a > 0 ? 0 : 1;
        }

        public double Function01(double x)
        {
           double y = Math.Exp(x) - Math.Exp(-x) / Math.Exp(x) + Math.Exp(-x);
            return y;
        }

        //////////////    Neuron Template   ///////////
        public double NeuronNAND(double in1, double in2, double in3, double w1, double w2, double w3, double bias)
        {
            return bias + (in1 * w1) + (in2 * w2) + (in3 * w3);

        }

        public double NeuronNot(double in1, double w1, double bias)
        {
            return bias + (in1 * w1);

        }


        public static double NAND(double in1, double in2, double in3)
        {

          
            double b = BIAS + (in1 * W1) + (in2 * W2) + (in3 * W3);

            double Sigmoide(double a)
            {
                return a > 0 ? 0 : 1;
            }

            double x = Sigmoide(b);
            Console.WriteLine("\n  " + in1 + " " + in2 + " " + in3);
   
            return x;
        }

    }//End class
}
