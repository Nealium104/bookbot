def get_num_characters(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def get_num_words(text):
    words = text.split()
    return len(words)
