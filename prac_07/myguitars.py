from guitar import Guitar

def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def save_guitars(filename, guitars):
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def display_guitars(guitars):
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")

def main():
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

    print("\nAdd new guitars:")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    guitars.sort()
    display_guitars(guitars)
    save_guitars("guitars.csv", guitars)

main()
