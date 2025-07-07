def read_wimbledon_data(filename):
    """Read the Wimbledon champions data from a CSV file."""
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            data = line.strip().split(',')
            year = data[0]
            country = data[1]
            champion = data[2]
            champions_data.append((year, country, champion))
    return champions_data


def count_champions(champions_data):
    """Count the number of titles for each champion."""
    champion_count = {}
    for _, _, champion in champions_data:
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1
    return champion_count


def get_countries(champions_data):
    """Get a sorted set of countries of the champions."""
    countries = set()
    for _, country, _ in champions_data:
        countries.add(country)
    return sorted(countries)


def main():
    # Count the champions and Print the champions in the order they appear in the data
    filename = 'wimbledon.csv'
    champions_data = read_wimbledon_data(filename)

    champion_count = count_champions(champions_data)

    print("Wimbledon Champions:")
    for champion, count in champion_count.items():
        print(f"{champion} {count}")

    countries = get_countries(champions_data)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()