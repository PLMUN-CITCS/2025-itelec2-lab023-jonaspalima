def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()  # Split the sentence by whitespace to get a list of words
    print(f"The sentence has {len(words)} words.")

def main():
    count_words()

if __name__ == "__main__":
    main()
