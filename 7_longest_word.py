# Longest Word Finder
# Given a sentence, find and print the longest word.

def find_longest_word(sentence_str):
    longest_word = ""
    current_word_length = 0
    longest_word_length = 0
    current_word_start_index = 0

    for i in range(len(sentence_str)):
        char = sentence_str[i]

        # If the character is a space or at the end of the sentence, it means a word has ended.
        if char == ' ' or i == len(sentence_str) - 1:
            # If it's the end of the sentence and not a space, include the last character in the word.
            if char != ' ':
                current_word_length += 1
        
            current_word = sentence_str[current_word_start_index : current_word_start_index + current_word_length]

            # If this word is longer than the current longest, update.
            if current_word_length > longest_word_length:
                longest_word_length = current_word_length
                longest_word = current_word
            
            # Reset for the next word.
            current_word_length = 0
            current_word_start_index = i + 1
        else:
            current_word_length += 1
            
    return longest_word

sentence_input = input("Enter sentence: ")

longest_found_word = find_longest_word(sentence_input)

print("Longest word is: ", longest_found_word)