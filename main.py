def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    number_of_words = get_number_of_words(book_text)
    char_count = get_number_of_characters(book_text)
    sorted_char_count = sorted_dictionary(char_count)
    generated_report = report_generation(sorted_char_count, number_of_words)
    print(generated_report)

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

def sorted_dictionary(char_count):
    character_list = [{"character": char, "num": count} for char, count in char_count.items() if char.isalpha()]

    character_list.sort(key=lambda x: x["num"], reverse=True)
    return character_list

def report_generation(sorted_char_count, number_of_words):
    report_words = [f"{number_of_words} words found in the book.\n"]

    for char in sorted_char_count:
        report_words.append(f"This '{char['character']}' was used {char['num']} times.")

    full_report = "--- Begin report of books/frankenstein.txt ---\n" + "\n".join(report_words) + "\n--- End of report ---"
    return full_report

main()