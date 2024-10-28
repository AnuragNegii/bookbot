from re import A, split

def main():
    book_path = "books/frankestein.txt"
    book = read_book_data(book_path)
    list_of_words_in_book = split_the_words(book)
    number_of_words = length_of_book(list_of_words_in_book)
    word = "THIS"
    list_of_char ={}
    list_of_char = number_of_chars_in_book(word, list_of_words_in_book)
    print()
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print()
    for i in list_of_char:
        print(f"The '{i}' character was found {list_of_char[i]} times")
    print("--- End report ---")


def read_book_data(path):
    with open(path) as f:
        return f.read()

def split_the_words(book):
    words_in_book = book.split()
    return words_in_book

def length_of_book(list_of_words):
    return len(list_of_words)

def number_of_chars_in_book(word, book_word_list):
    words = word.lower()
    a = {}
    for w in words:
        a[w] = 0
    
    for w in book_word_list:
        for i in w:
            if i in a:
                a[i] += 1

    return a

main() 
