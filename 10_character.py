# Character Counter
# Count how many times each character appears in a string (excluding spaces).

def count_characters(input_string):
    char_counts = {}

    for char in input_string:
        if char != ' ':  
            found = False
            for existing_char in char_counts:
                if existing_char == char:
                    char_counts[existing_char] += 1
                    found = True
                    break
            if not found:
                char_counts[char] = 1
    return char_counts

text = "Hello World"
counts = count_characters(text)
print(f"Character counts for '{text}': {counts}")

text2 = "Python is innteresting coding language"
counts2 = count_characters(text2)
print(f"Character counts for '{text2}': {counts2}")

text3 = "aabbcdeeff"
counts3 = count_characters(text3)
print(f"Character counts for '{text3}': {counts3}")

text4 = "   " # An empty string or just spaces.
counts4 = count_characters(text4)
print(f"Character counts for '{text4}': {counts4}")