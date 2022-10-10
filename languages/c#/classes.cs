using System;

namespace Vehicules
{
    interface Vehicule
    {
        void move();
        string toString();
    }

    public abstract class WheeledVehicule: Vehicule
    {
        // Give access only to subclasses
        private string brand;
        protected int numberWheels;

        public string Brand
        {
            get { return brand; }
            set { brand = value; }
        }

        public abstract void move();

        public virtual string toString()
        {
            return $"I am a {brand} vehicule with {numberWheels} wheels.";
        }
    }

    public class Car: WheeledVehicule
    {
        public Car(string brand, int numberWheels = 4)
        {
            base.Brand = brand;
            base.numberWheels = numberWheels;
        }

        public override void move()
        {
            Console.WriteLine("The car is advancing.");
        }
    }

    public class Bike: WheeledVehicule
    {
        public Bike(string brand, int numberWheels = 2)
        {
            base.Brand = brand;
            base.numberWheels = numberWheels;
        }

        public override void move()
        {
            Console.WriteLine("The bike is advancing.");
        }
    }
}

namespace Programs
{
    class Program
    {
        static void Main(string[] args)
        {
            Vehicules.Car myCar = new Vehicules.Car("Mercedes");
            Vehicules.Bike myBike = new Vehicules.Bike("Cannondale");

            myCar.move();
            Console.WriteLine(myCar.toString());

            myBike.move();
            Console.WriteLine(myBike.toString());
        }
    }
}