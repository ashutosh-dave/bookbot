from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    """Main function to read the book and count words and characters."""
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()

