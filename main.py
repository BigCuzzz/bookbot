from stats import get_num_words, get_num_chars, sort_chars_dict
import sys

print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    found_chars = get_num_chars(text)
    sorted_chars = sort_chars_dict(found_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch in sorted_chars:
        if ch["char"].isalpha():
            print(f'{ch["char"]}: {ch["num"]}')
        else:
            pass
    #print(found_chars)
    #print(sorted_chars)
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()