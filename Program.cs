/*
Programmer: Antony Melendez
Description: juest testing 
Date: 09/24/20
*/
using System;
namespace School
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the following info: ");
            Console.WriteLine("Total items in menu: ");
            int mItems = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Total drink: ");
            int dItems = Convert.ToInt32(Console.ReadLine());

            float tip = 0.15f;
            float mPrice = 1.75f;
            float dPrice = 1f;

            float mTotal = mItems * mPrice;
            float dTotal = dItems * dPrice;


            float aTotal = mTotal + dTotal * tip;

            Console.WriteLine("Your total is: $" + aTotal);
        }
    }
}
