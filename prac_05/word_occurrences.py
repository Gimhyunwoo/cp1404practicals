def main():
    # sorts the words alphabetically, and prints each word with its count.
    text = input("Text: ").lower()

    word_counts = {}
    words = text.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.keys())

    for word in sorted_words:
        print(f"{word} : {word_counts[word]}")


main()