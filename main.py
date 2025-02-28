from stats import (
    count_words, 
    get_book_text, 
    count_characters, 
    sorted_dictionaries
)

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    total = count_words(text)
    counts = count_characters(text)
    order = sorted_dictionaries(counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath,"...")
    print("----------- Word Count ----------")
    print(f"{total} words found in the document")
    print("--------- Character Count -------")
    print(order)
    print("============= END ===============")
    
main()