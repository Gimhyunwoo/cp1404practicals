"""guitar_test.py

Estimated: 7 minutes
Actual: 6 minutes
"""

from guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 500)

    print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 12. Got {another.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

if __name__ == '__main__':
    main()
