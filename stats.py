def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return(file_contents)

def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    counts = {}
    lowercase_text = text.lower()
    for i in lowercase_text:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

def sorted_dictionaries(counts):
    counts.sort(reverse=True, key=lambda x: list(x.value())[1])
    return counts