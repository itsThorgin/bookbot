def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    number_of_words = get_number_of_words(book_text)
    char_count = get_number_of_characters(book_text)
    print(f"This book has {number_of_words} words.")
    print(f"These are the characters used in the book: {char_count}")

def get_book_text(path_to_book):
    with open(path_to_book) as book:
        book_text = book.read()
    return book_text

def get_number_of_words(book_text):
    words = book_text.split()
    return len(words)

def get_number_of_characters(book_text):
    words_to_lower = book_text.lower()
    dictionary = {}

    for char in words_to_lower:
        count = dictionary.get(char, 0)
        dictionary[char] = count + 1
    return dictionary

main()