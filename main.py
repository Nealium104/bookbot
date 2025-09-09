import sys
from stats import get_num_words, get_num_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_characters(text)
    report = get_report(get_num_characters(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(f"{report}")
#    print(f"{num_words} words found in the document. All letters: {num_char}. Report: {report}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_report(chars):
    def sort_on(dict):
        return dict[1]

    sorted_chars = sorted(chars.items(), reverse=True, key=sort_on)
    report = ''
    for char, count in sorted_chars:
        if char.isalpha():
            report += f"{char}: {count}\n"
    return report

main()
