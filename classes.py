''''
Customize the value behaviour of drive:
Inside ElectricCar class:
    redefine the drive(self, distance) function again.
    it will have the same behaviour regarding 'milage_km"
    but add at the end some code so that self.range gets subtracted
    by the drive 'distance.'
Test the drive behaviour of ElectricCar class:
    initialize an object from ElectricCar class "my_ev"
    call 'my_ev.drive(some_distance) a few times
    notice via print(my_ev.__dict__) that the range has been reduced.
   
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
class Car:
    
    def __init__(self, brand:str, milage_km:int) -> None:
        assert milage_km > 0, "milage_km can't be less than 0"
        self.brand = brand
        self.milage_km = milage_km

    def drive(self, distance_km:float):
        assert distance_km > 0,  f"distance_km must be greater than 0 (got {distance_km})"        
        self.milage_km += distance_km


class ElectricCar(Car):

    def __init__(self, brand:str, milage_km:int, range:int) -> None:
        super().__init__(brand, milage_km)
        assert range > 0, "range must be greater than 0"
        self.range = range

    def drive(self, distance_km: float):
        super().drive(distance_km)
        new_range = self.range - distance_km
        assert new_range > 0, "Oh no! You've run out of battery!"
        self.range = new_range

my_ev_car = ElectricCar(brand='tesla', milage_km=200, range=20000)
my_ev_car.drive(distance_km=100)
assert my_ev_car.milage_km == 300, "Expected milage_km to be 300"
assert my_ev_car.range == 19900, f"Expected range to be 19900 but got {my_ev_car.range}"

my_ev_car.drive(distance_km=20)
assert my_ev_car.milage_km == 320, "Expected milage_km to be 320"
assert my_ev_car.range == 19880, "Expected range to be 19880"

my_ev_car.drive(distance_km=200)
assert my_ev_car.milage_km == 520, "Expected milage_km to be 520"
assert my_ev_car.range == 19680, "Expected range to be 19680"

# For both EV and ICE cars distance_km can't be less than 0 when calling drive()
try:
    my_ev_car.drive(distance_km= -1)
except Exception as e:
    print(e)

try:
    # For EVs drive() method should not set range to a value less than 0 
    my_ev_car.drive(20001)
except Exception as e:
    print(e)

try:    
    # For both EV and ICE cars milage_km can't be less than 0
    my_crapped_out_ev_car = ElectricCar(brand='tesla', milage_km=-1, range=20000)
except Exception as e:
    print(e)    

try:
    # For EVs range cannot be less than 0
    my_other_crapped_out_ev_car = ElectricCar(brand='tesla', milage_km=100, range=-1)
except Exception as e:
    print(e)    

print(my_ev_car.__dict__)

'''
Inside IceCar class:
    redefine the drive(self, distance) function again.
    it will have the same behaviour regarding 'milage_km"
    but add at the end some code so that self.fuel_level gets subtracted
    by the drive distance*fuel_consumption/100 (how much fuel
    we will consume)
Test the drive behaviour of IceCAr class:
    initialize an object from IceCar class "my_ice_car"
    call 'my_ice_car.drive(some_distance) a few times
    notice via print(my_ice_car.__dict__) that the fuel level has been reduced.
'''
class IceCar(Car):
    def __init__(self, brand:str, milage_km:int, fuel_consumption:float, fuel_level:float) -> None:
        Car.__init__(self, brand, milage_km)
        assert fuel_consumption > 0
        assert fuel_level > 0
        self.fuel_consumption = fuel_consumption
        self.fuel_level = fuel_level

    def drive(self, distance_km: float):
        super().drive(distance_km)
        new_fuel_level = self.fuel_level - (distance_km * self.fuel_consumption / 100)
        assert new_fuel_level > 0, "Oh no! You've run out of petrol!"
        self.fuel_level = new_fuel_level

my_ice_car = IceCar(brand='V8', milage_km=100, fuel_consumption=100, fuel_level=2000)

my_ice_car.drive(distance_km = 50)
assert my_ice_car.milage_km == 150
assert my_ice_car.fuel_level == 1950.0

my_ice_car.drive(distance_km = 100)
assert my_ice_car.milage_km == 250
assert my_ice_car.fuel_level == 1850.0

my_ice_car.drive(distance_km = 200)
assert my_ice_car.milage_km == 450
assert my_ice_car.fuel_level == 1650.0

try:
    # For both EV and ICE cars distance_km can't be less than 0 when calling drive()
    my_ice_car.drive(distance_km= -1)
except Exception as e:
    print(e)

try:
    # For ICE cars drive() method should not set fuel level to a value less than 0 
    my_ice_car.drive(50000)
except Exception as e:
    print(e)

try:
    # For both EV and ICE cars milage_km can't be less than 0
    my_crapped_out_ice_car = IceCar(brand='V8', milage_km=-1, fuel_consumption=100, fuel_level=2000)
except Exception as e:
    print(e)

try:    
    # For ICE cars fuel consumption cannot be less than 0
    my_other_crapped_out_ice_car = IceCar(brand='V8', milage_km=-1, fuel_consumption=-1, fuel_level=2000)
except Exception as e:
    print(e)
          
try:     
    # For ICE cars fuel level cannot be less than 0
    my_really_crapped_out_ice_car = IceCar(brand='V8', milage_km=1000, fuel_consumption=100, fuel_level=-1)
except Exception as e:
    print(e)


print(my_ice_car.__dict__)


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

import math

class Shape:

    def area() -> None:
        pass

class Triangle(Shape):

    def __init__(self, side_a:int, side_b:int, side_c:int) -> None:
        super().__init__()

        # Put sides into an array, sort, then verify that the last
        sides_sorted = sorted([side_a, side_b, side_c], reverse=True)
        
        assert sides_sorted[2] > 0, "Length of each side of the triangle should be greater than 0."
        assert sides_sorted[0] < sides_sorted[1] + sides_sorted[2], f"Length of the longest side ({sides_sorted[0]} should be less than the sum of the other two sides {sides_sorted[1]}+{sides_sorted[2]})"

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self) -> float:
        # Determine perimeter
        p = sum([self.side_a, self.side_b, self.side_c])
        # Determine the semiperimeter
        s = p / 2
        # Use Heron's formula to find the area of the triangle
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

my_triangle = Triangle(side_a = 60, side_b = 40, side_c = 80)
assert int(my_triangle.area()) == 1161, f"Incorrect area for triangle, expected but got {int(my_triangle.area)}"

try:
    # Sides cannot be less than 0
    my_faulty_triangle = Triangle(side_a = 60, side_b = -40, side_c = 80)
except Exception as e:
    print(e)

class Rectangle(Shape):

    def __init__(self, side_a: int, side_b: int) -> int:
        super().__init__()
        assert side_a > 0 and side_b > 0, "Each side of the reactangle should be greater than 0"
        assert side_a != side_b, "Sides of the reactangle should not be equal"
        self.side_a = side_a
        self.side_b = side_b

    def area(self) -> int:
        return self.side_a * self.side_b

my_reactangle = Rectangle(20, 50)
area_of_reactangle = my_reactangle.area()
assert area_of_reactangle == 1000, "Expected area of rectangle to be 1000 but got {area_of_reactangle}"
           
try:
    my_invalid_reactangle = Rectangle(-1, 100)        
except Exception as e:
    print(e)

try:
    my_invalid_reactangle = Rectangle(100, -1)        
except Exception as e:
    print(e)

try:
    is_really_a_square = Rectangle(100, 100)        
except Exception as e:
    print(e)

class Circle(Shape):

    def __init__(self, radius:int):
        super().__init__()
        assert radius > 0, "Radius must be greater than 0"
        self.radius = radius

    def area(self) -> int:
        # area = pi * (radius squared)
        return math.pi * pow(self.radius, 2)

my_circle = Circle(100)
area_of_circle = my_circle.area()
assert int(area_of_circle) == 31415, f"Expected area of circle to be 31415 but got {area_of_circle}"

try:
    my_invalid_circle = Circle(-10)
except Exception as e:
    print(e)

'''
modules
data classes
abstract base classes
apply to Shape exercise
'''