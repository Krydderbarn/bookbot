from stats import *
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")

        # Word count section
        print("----------- Word Count ----------")
        print(get_num_words(file_path))

        # Character count section
        print("--------- Character Count -------")
        sorted_char_list = sort_stats(file_path)

        for item in sorted_char_list:
            char = item["char"]
            count = item["num"]

            if char.isalpha():  # Only print alphabetic characters
                print(f"{char}: {count}")

        print("============= END ===============")


main()