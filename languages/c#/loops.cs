using System;

namespace MainSpace
{
  class Program
  {
    static void Main(string[] args)
    {
        // For loop
        Console.WriteLine("Looping a regular for loop.");
        for (int i = 0; i < 10; i++) 
        {
            Console.WriteLine(i);
        }

        // Foreach with an array
        int[] arr = {1, 2, 3, 4, 5};
        Console.WriteLine("Looping a foreach loop.");
        foreach (int val in arr)
        {
          Console.WriteLine(val);
        }

        // While in an array
        int count = 0;
        Console.WriteLine("Looping with a while loop.");
        while (count <= 4)
        {
          Console.WriteLine(arr[count]);
          count++;
        }
    }
  }
}