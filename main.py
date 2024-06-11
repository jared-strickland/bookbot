def count_characters(text):
    character_counts = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char.isalpha():  # Only count alphabetical characters
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1

    return character_counts

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)

        # Count characters
        char_counts = count_characters(file_contents)

        # Sort characters by count in descending order
        sorted_char_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

        # Print the report
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document\n")
        
        for char, count in sorted_char_counts:
            print(f"The '{char}' character was found {count} times")

        print("--- End report ---")

if __name__ == "__main__":
    main()
