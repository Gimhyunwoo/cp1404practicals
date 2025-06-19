import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    # Ask the user how many quick picks to generate.
    # Generate and display the quick picks
    quick_picks_count = int(input("How many quick picks? "))


    for _ in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print(format_quick_pick(quick_pick))


def generate_quick_pick():
    """Generate a single line of quick pick numbers."""
    unique_numbers = set()

    while len(unique_numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        unique_numbers.add(number)

    return sorted(unique_numbers)


def format_quick_pick(quick_pick):
    """Format the quick pick for display."""
    return ' '.join(f"{num:2}" for num in quick_pick)



main()