using System;
using IntroLibrary;

namespace IntroUI
{
    class Program
    {

        static void Main(string[] args)
        {
            greetUser();
            input();
        }

        private static void greetUser()
        {
            Console.WriteLine("Welcom!");
            Console.WriteLine("Please enter the following inputs: ");
        }

        static void input()
        {
            Console.WriteLine("Enter you first name: ");
            personModel.FirstName = Console.ReadLine();
            Console.WriteLine("Enter you last name: ");
            personModel.LastName = Console.ReadLine();
            Console.WriteLine("Enter you age: ");
            personModel.Age = Convert.ToInt32(Console.ReadLine());

            exitProgram();
        }

        private static void exitProgram()
        {
            Console.WriteLine("Goodbye!");
        }
    }
}