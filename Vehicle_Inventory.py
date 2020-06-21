#This is a simple inventory program for a small car dealership.
print('Automotive Inventory')
class Automobile:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = 0
    def addVehicle(self):
        try:
            self._make = input('Enter vehicle make: ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle year: '))
            self._color = input('Enter vehicle color: ')
            self._mileage = int(input('Enter vehicle mileage: '))
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for mileage and year')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._year, self._color, self._mileage])

class Inventory:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('This vehicle has been added, Thank you')
    def viewInventory(self):
        print('\t'.join(['','Make', 'Model','Year', 'Color', 'Mileage']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)

inventory = Inventory()
while True:

    print('#1 Add Vehicle to Inventory')
    print('#2 Delete Vehicle from Inventory')
    print('#3 View Current Inventory')
    print('#4 Update Vehicle in Inventory')
    print('#5 Export Current Inventory')
    print('#6 Quit')
    userInput=input('Please choose from one of the above options: ') 
    if userInput=="1": 
        #add a vehicle
        inventory.addVehicle()
    elif userInput=='2':
        #delete a vehicle
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Please enter the number associated with the vehicle to be removed: '))
        if item - 1  > len(inventory.vehicles):
            print('This is an invalid number')
        else:
            inventory.vehicles.remove(inventory.vehicles[item - 1])
            print ()
            print('This vehicle has been removed')
    elif userInput == '3':
        #list all the vehicles
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.viewInventory()
    elif userInput == '4':
        #edit vehicle 
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Please enter the number associated with the vehicle to be updated: '))
        if item - 1  > len(inventory.vehicles):
            print('This is an invalid number')
        else:
            automobile = Automobile()
            if automobile.addVehicle() == True :
                inventory.vehicles.remove(inventory.vehicles[item - 1])
                inventory.vehicles.insert(item - 1, automobile)
                print ()
                print('This vehicle has been updated')
    elif userInput == '5':
        #export inventory to file
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        f = open('vehicle_inventory.txt', 'w')
        f.write('\t'.join(['Make', 'Model','Year', 'Color', 'Mileage']))
        f.write('\n')
        for vechicle in inventory.vehicles:
            f.write('%s\n' %vechicle)
        f.close()
        print('The vehicle inventory has been exported to a file')
    elif userInput == '6':
        #exit the loop
        print('Goodbye')
        break
    else:
        #invalid user input
        print('This is an invalid input. Please try again.')
