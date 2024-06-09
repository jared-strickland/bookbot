def count_characters(text):
    character_counts = {}
    lowered_text = text.lower()

    for char in lowered_text:
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
        print(f"Number of words: {num_words}")

        # Count characters
        char_counts = count_characters(file_contents)
        print(char_counts)

if __name__ == "__main__":
    main()

