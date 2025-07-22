from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Expected fare: $48.80, Actual fare: ${fare:.2f}")
    assert round(fare, 2) == 48.80, "Fare calculation failed"

test_silver_service_taxi()
