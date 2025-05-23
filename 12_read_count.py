# Read and Count Words
# Read a text file and count total words, lines, and characters.

import os
def analyze_text_file(filename="file.txt"):
    total_lines = 0
    total_words = 0
    total_characters = 0

    print(f"--- Analyzing '{filename}' ---")
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found in the current directory.")
        print("Please make sure 'file.txt' is in the same folder as this script.")
        return 

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                total_lines += 1
                total_characters += len(line) # Count all characters, including spaces and newlines.
                
                # Manually split the line into words.
                current_word = ""
                words_in_line = []
                for char in line:
                    # A word ends when we hit a space or newline, or it's the end of the line.
                    if char == ' ' or char == '\n' or char == '\r':
                        if current_word:
                            words_in_line.append(current_word)
                        current_word = ""
                    else:
                        current_word += char
                if current_word: # Add the very last word of the line if it's not empty.
                    words_in_line.append(current_word)

                total_words += len(words_in_line)

        print("\n--- Analysis Results ---")
        print(f"Total Lines: {total_lines}")
        print(f"Total Words: {total_words}")
        print(f"Total Characters (including spaces and newlines): {total_characters}")

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    analyze_text_file("file.txt")