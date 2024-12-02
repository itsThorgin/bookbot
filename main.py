def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    number_of_words = get_number_of_words(book_text)
    print(f"This book has {number_of_words} words.")

def get_book_text(path_to_book):
    with open(path_to_book) as book:
        book_text = book.read()
    return book_text

def get_number_of_words(book_text):
    words = book_text.split()
    return len(words)

main()