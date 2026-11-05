import sys

from stats import chars_dict_to_sorted_list, get_char_dict, get_word_count


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def print_report(book_path: str, word_count: int, sorted_list: list):
    print(f'''
============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Wordcount -----------
Found {word_count} total words
--------- Character Count -------''')

    for char in sorted_list:
        if char[0].isalpha() == True:
            print(f"{char[0]}: {char[1]}")

    print("========== End ===============")

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    char_dict = get_char_dict(book_text)
    char_list_sorted = chars_dict_to_sorted_list(char_dict)

    print_report(book_path, num_words, char_list_sorted)

main()
