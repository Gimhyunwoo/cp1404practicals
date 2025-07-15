from programming_language import ProgrammingLanguage

def main():
    languages = []
    with open("languages.csv", "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split(",")
            name, typing = parts[0], parts[1]
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[3] == "Yes"
            language = ProgrammingLanguage(name, typing, reflection, pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)

main()
