from unreliable_car import UnreliableCar

def test_unreliable_car():
    car = UnreliableCar("Unreliable", 100, 50)
    total_driven = 0
    for _ in range(100):
        total_driven += car.drive(1)
    print(f"Total driven (should be ~50 if 50% reliable): {total_driven}")

test_unreliable_car()
