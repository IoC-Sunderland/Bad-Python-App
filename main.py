""" Vince's Vehicles:

This system allows the user to rent different types of vehicles
and manage inventory.

"""

import sys

def print_mm():

    print("""
            1.Add a Vehicle to Inventory
            2.Remove a Vehicle from Inventory
            3.View all Vehicles in Inventory
            4.View Rental Log
            5.Rent a Vehicle
            6.Exit/Quit
            """)

    ans = input("What would you like to do? ")

    if ans == "1":
        vehicle = input("Enter vehicle type, choose from:\n" + "1: Car\n" + "2: Plane\n" + "3: Boat\n" + "\nChoice: ")

            # Car
        if vehicle == "1":
            print('\nEnter Car details:\n')
            colour = input("Car Colour: ")
            weight = int(input("Car Weight: "))
            brand = input("Brand: ")

            car = Car(colour, weight,brand)

            VehicleInventory.ALL_VEHICLES.append(car)

            print_mm()
        elif vehicle == "2":
            print('\nEnter Plane details:\n')
            colour = input("Plane Colour: ")
            weight = int(input("Plane Weight: "))
            brand = input("Brand: ")

            vehicle = Plane(colour,weight,brand)

            VehicleInventory.ALL_VEHICLES.append(vehicle)

            print_mm()
        elif vehicle == "3":
            print('\nEnter Boat details:\n')
            colour = input("Boat Colour: ")
            weight = int(input("Boat Weight: "))
            brand = input("Boat Brand: ")
            motor_type = input("Motor Type: ")

            boat = Boat(colour,weight,brand,motor_type)

            VehicleInventory.ALL_VEHICLES.append(boat)

            print_mm()
    elif ans == "2":
        vehicle_to_remove = int(input('Vehicle number to be removed: '))
        idx_of_vehicle = vehicle_to_remove - 1
        del VehicleInventory.ALL_VEHICLES[idx_of_vehicle]
        print_mm()
    elif ans == "3":
        print('\n')
        print("All vehicles in inventory...\n")
        for (i, item) in enumerate(VehicleInventory.ALL_VEHICLES, start=1):
            print(i, item)
        print_mm()

    #   Current rentals
    elif ans == "4":
        print('\n')
        print('Currently rented vehicles...\n')
        for (i, item) in enumerate(Rentals.CURRENT_RENTALS, start=1):
            print(i, item)
        print_mm()


    elif ans == "5":
        print('\n')
        print("All vehicles available to rent: \n")
        for (i, item) in enumerate(VehicleInventory.ALL_VEHICLES, start=1):
            print(i, item)
        vehicle_to_rent = int(input('\nWhich vehicle number do you want to rent: '))
        vehicle_idx = vehicle_to_rent -1
        Rentals(vehicle_idx)
        print_mm()
    elif ans == "6":
        sys.exit()
    elif ans != "":
        print("\n Not Valid Choice Try again")
        print_mm()

class VehicleInventory:
    """Holds a list of all vehicles"""
    ALL_VEHICLES = []

    def __init__(self, new_vehicle):

        VehicleInventory.ALL_VEHICLES.append(new_vehicle)

class Rentals: 
   
    CURRENT_RENTALS = []

    def __init__(self, vehicle):
        vehicle = VehicleInventory.ALL_VEHICLES[vehicle]
        VehicleInventory.ALL_VEHICLES.remove(vehicle)
        Rentals.CURRENT_RENTALS.append(vehicle)


class Vehicle:
    """ A Vehicle Class """

    vehicle_count = 1

    VEHICLE_TYPES = []

    def __init__(self, colour, weight, brand):
        # Attributes that are common across all vehicles
        self.colour = colour
        self.weight = weight
        self.brand = brand
        self.vehicle_number = f'VV{str(Vehicle.vehicle_count)}'
        Vehicle.vehicle_count += 1

    def __str__(self):

        return "\nVehicle Number: " + self.vehicle_number + "Vehicle Type: " + self.__class__.__name__ + "\n" + \
                                "Colour:" + self.colour + "\n" \
                              + "Weight:" + str(self.weight) + "\n" \
                              + "Brand:" + self.brand + "\n"

    def __repr__(self):

        return "Vehicle()"


class Car(Vehicle): 
    def __init__(self, colour, weight, brand):
        self.colour = colour
        self.weight = weight
        self.brand = brand
        self.vehicle_number = f'VV{str(Vehicle.vehicle_count)}'
        Vehicle.vehicle_count += 1


class Boat(Vehicle):  

    def __init__(self, colour, weight, brand, motor_type):

        self.motor_type = motor_type
        self.colour = colour
        self.weight = weight
        self.brand = brand
        self.vehicle_number = f'VV{str(Vehicle.vehicle_count)}'
        Vehicle.vehicle_count += 1

    def __str__(self):
        return "This is a Boat object" 

    def __repr__(self):
        return "Vehicle()"


class Plane(Vehicle):  
    """ A Plane Class """


print_mm()
