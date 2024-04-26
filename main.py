def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_characters(text)
    report = get_report(get_num_characters(text))
    print(f"{num_words} words found in the document. All letters: {num_char}. Report: {report}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def get_report(chars):
    def sort_on(dict):
        return dict[1]
    
    sorted_chars = sorted(chars.items(), reverse=True, key=sort_on)
    report = ''
    for char, count in sorted_chars:
        if char.isalpha():
            report += f"The {char} was found {count} times\n"
    return report

main()