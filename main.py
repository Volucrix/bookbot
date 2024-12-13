def get_book(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    return len(book.split())

def count_characters(book):
    alphabet = {}
    for character in book:
        lowercase_letter = character.lower()
        if lowercase_letter in alphabet:
            alphabet[lowercase_letter] += 1
        else:
            alphabet[lowercase_letter] = 1
    return alphabet


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {word_count} words in this book")
    for character in character_count:
        print(f"The '{character}' character was found {character_count[character]} times")
    print("--- End Report ---")

main()