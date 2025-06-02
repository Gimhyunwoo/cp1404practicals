def main():
    score = get_valid_score()
    choice = ""

    while choice != "Q":
        choice = input("Menu\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit: ").upper()

        if choice == "G":
            score = get_valid_score()

        elif choice == "P":
            result = print_result(score)
            print(result)

        elif choice == "S":
            print("*" * score)

        elif choice == "Q":
            print("Farewell")

        else:
            print("Invalid choice. Choose again.")

def get_valid_score():
    score = int(input("Type your score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Type your score (0-100): "))
    return score

def print_result(score):
    """Return a result string based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
