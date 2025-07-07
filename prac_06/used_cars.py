"""used_cars.py

Estimated: 5 minutes
Actual: 4 minutes
"""

from car import Car

def main():
    limo = Car("Limo", 100)
    limo.add(20)
    print(f"Fuel after adding: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Attempted to drive 115km, actually drove: {distance_driven}km")
    print(limo)

if __name__ == '__main__':
    main()
