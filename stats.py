def get_word_count(file_content: str) -> int:
    words = file_content.split()
    word_count = len(words)
    return word_count

def get_char_dict(book_text: str) -> dict[str, int]:
    lowered_text = book_text.lower()
    char_dict: dict = {}

    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(chars: tuple[str, int]) -> int:
    return chars[1]

def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars_list = []

    for char_key, char_count in char_dict.items():
        char_tuple = (char_key, char_count)
        chars_list.append(char_tuple)

    sorted_chars: list[tuple[str, int]] = sorted(chars_list, reverse=True, key=sort_on)

    return sorted_chars
