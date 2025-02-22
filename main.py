from stats import *
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <book_file>")
        sys.exit(1)

    book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    
    # Get word count
    w_count = word_count(book)
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    
    # Get character count and sort it
    c_count = character_count(book)
    sorted_chars = sorted(c_count.items(), key=sort_on, reverse=True)

    print("--------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")

    print("============= END ===============")

main()


