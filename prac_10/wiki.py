"""
Prac 10 - Wikipedia API usage
"""

import wikipedia

def main():
    while True:
        search_phrase = input("Enter page title: ").strip()
        if not search_phrase:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(search_phrase, sentences=2))
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()
