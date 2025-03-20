def count_words(text):
    """Counts the number of words in the given text."""
    return len(text.split())

def count_characters(text):
    """Counts the occurrences of each character in the given text."""
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_characters(char_counts):
    """Sorts characters by count in descending order."""
    sorted_chars = [{"char": char, "count": count} for char, count in char_counts.items()]
    sorted_chars.sort(key=lambda x: x["count"], reverse=True)
    return sorted_chars

