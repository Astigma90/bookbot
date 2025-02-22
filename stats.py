def get_book_text(file):
    with open(file) as f:
        book = f.read()
        return book

def word_count(file):
    book = get_book_text(file)
    words = book.split()
    return len(words)  # Simplified counting

def character_count(file):
    with open(file) as f:
        book = f.read()
        character_dic = {}
        for c in book:
            c = c.lower()
            if c.isalnum():
                character_dic[c] = character_dic.get(c, 0) + 1
    return character_dic

def sort_on(item):
    return item[1]  # Sort by count (second item in tuple)
