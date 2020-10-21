using System;
using IntroLibrary;

namespace IntroUI
{
    class Program
    {

        public static void Main(string[] args)
        {
            input();
            Console.WriteLine("\n***********************************************************");

            //endProgram();
            Console.WriteLine("\n***********************************************************");
        }

        public static void input()
        {
            Console.WriteLine("Enter you first name: ");
            personModel.FirstName = Console.ReadLine();
            Console.WriteLine("Enter you last name: ");
            personModel.LastName = Console.ReadLine();
            Console.WriteLine("Enter you age: ");
            personModel.Age = Convert.ToInt32(Console.ReadLine());

            greetUser();
            Console.WriteLine("\n***********************************************************");
        }

        private static void greetUser()
        {
            Console.WriteLine("Hello ", personModel.FirstName, "", personModel.LastName, " your age is: ", personModel.Age);
        }

        private static void endProgram()
        {
            Console.WriteLine("\n***********************************************************");
            Console.WriteLine("Goodbye!");
            //System.Environment.Exit(0);
        }
    }
}