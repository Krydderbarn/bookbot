def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    contents = get_book_text(file_path)
    num_words = len(contents.split())
    return f"Found {num_words} total words"

def get_unique_chars(file_path):
    contents = get_book_text(file_path).lower()
    unique_dictionary = {}

    for char in contents:
        if char in unique_dictionary:
            unique_dictionary[char] += 1
        else:
            unique_dictionary[char] = 1

    return unique_dictionary

def sort_helper(items):
    return items["num"]

def sort_stats(file_path):
    char_counts = get_unique_chars(file_path)

    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(key=sort_helper, reverse=True)

    return char_list

