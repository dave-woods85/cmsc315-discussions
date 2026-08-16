"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Vehicle:
    """Creates a virtual vehicle"""
    DOT_approved = True

    def __init__(self, wheels=4, power=100, fuel='gas'):
        """This is a constructor for a vehicle object.

        wheels      number of wheels
        power       how much horsepower the vehicle has
        fuel        fuel type for the vehicle (gas, diesel, electric)
        """
        self._wheels = wheels
        self._power = power
        self._fuel = fuel

    def get_wheels(self):
        """returns number of wheels"""
        return self._wheels

    def get_power(self):
        """returns the power of the vehicle"""
        return self._power

    def get_fuel(self):
        """Returns the fuel type"""
        return self._fuel

    



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.




class Car(Vehicle):
    """A specific vehicle type"""
    displacement = 0

    def __init__(self, wheels, power, fuel, doors=2, occupancy=2):
        """Creates a car

        doors      specifies number of doors for 2:coupe, 3:hatchback, 4:sedan, 5:wagon)
        occupancy   how many seats are in the vehicle
        """
        super().__init__(wheels, power, fuel)
        self._doors = doors
        self._occupancy = occupancy

    def get_doors(self):
        """Returns door count"""
        return self._doors


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    """To demonstrate attributes within different namespaces"""

    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    new_sedan = Car(4, 250, 'diesel', 4, 5)
    new_coupe = Car(2, 350, 'gas', 2, 2)

    print(Car.get_doors(new_sedan))
    print(new_sedan.get_doors())

    new_coupe._power = 400

    print(new_coupe._power)
    print(new_coupe.__dict__) # Rough display of attributes
    print(new_sedan.__dict__) # Rough display of attributes






# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    """ To demonstrate the creation of shallow and deep copies of an object
    """
    print("\n==Copy Demonstration==")

    new_wagon = Car(4, 230, 'electric', 5, 5)

    wagon_copy = new_wagon # This creates an alias aka shallow copy that references the same object
    wagon_deep_copy = deepcopy(new_wagon) # This creates a new separate object with the attributes of the original

    new_wagon._occupancy = 4

    print(wagon_copy.__dict__) # when this one prints, it will reflect the change to the original new_wagon
    print(wagon_deep_copy.__dict__) # when this one prints out, it will not be affected by the change to new_wagon







if __name__ == "__main__":
    """This will run the necessary functions"""
    demonstrate_namespaces()
    demonstrate_copying()


