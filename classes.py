''''
Customize the value behaviour of drive:
Inside ElectricCar class:
    redefine the drive(self, distance) function again.
    it will have the same behaviour regarding 'milage_km"
    but add at the end some code so that self.range sets subtracted
    by the drive 'distance.'
Test the drive behaviour of ElectricCar class:
    initialize an object from ElectricCar class "my_ev"
    call 'my_ev.drive(some_distance) a few times
    notice via print(my_ev.__dict__) that the range has been reduce.
   
Inside IceCar class:
    redefine the drive(self, distance) function again.
    it will have the same behaviour regarding 'milage_km"
    but add at the end some code so that self.fuel_level sets subtracted
    by the drive distance*fuel_consumption/100 (how much fuel
    we will consume)
Test the drive behaviour of IceCAr class:
    initialize an object from IceCar class "my_ice_car"
    call 'my_ice_car.drive(some_distance) a few times
    notice via print(my_ice_car.__dict__) that the range has been reduce.
   
'''



''''
Create a parent class 'Shape'
    Only defined the def area() interface function.
        def area()
            pass
Create a child class of 'Shape'
    For example 'Triangle'
    Define how Triangle is constructed
        a, b, c
        assert that it is a valid triangle
    Define how area() is calculated
    Test out the definition of a Triangle + correct area 
    calculated.

Do the above for 3 more shapes.
'''

'''
modules
data classes
abstract base classes
apply to Shape exercise
'''