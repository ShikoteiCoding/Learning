using System;

namespace Variables
{
    class Program
    {
        static void Main() 
        {
            string text = "String Variable";
            Console.WriteLine("This is a string variable: " + text);    // C# can concatenate strings

            int number = 123;
            Console.WriteLine("This is an integer (" + number + ") with implicit cast."); // C# cast numbers to string implicitely
            Console.WriteLine("This is an integer (" + number.ToString() + ") with explicit cast."); // C# cast numbers to string implicitely

            double floatNumber = 19.99D;
            Console.WriteLine("This is a double: " + floatNumber);

            bool boolean = true;
            Console.WriteLine("This is a boolean: " + boolean);

            text += " Modified";
            Console.WriteLine("This is a string modified: " + text);

            const string constText = "String Constant";
            Console.WriteLine("This is a string constant: " + constText);
        }
    }
}