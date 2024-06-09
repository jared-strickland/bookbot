def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words =file_contents.split()
        num_words=len(words)
    print (f"Number of words: {num_words}")

if __name__ == "__main__":
    main()
