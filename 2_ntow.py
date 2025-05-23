# Number to Words Converter
# Convert a number (e.g., 123) into its word form ("one hundred twenty-three").

def convert_num_to_words(number_val):
    if not isinstance(number_val, int):
        return "" # Input isn't an integer

    if number_val == 0:
        return "zero"

    is_negative = False
    if number_val < 0:
        is_negative = True
        number_val = abs(number_val) # Process absolute value

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    magnitudes = ["", "thousand", "million", "billion", "trillion"]

    def process_block(val_in_block):
        if val_in_block == 0:
            return ""
        if val_in_block < 10:
            return units[val_in_block]
        elif val_in_block < 20:
            return teens[val_in_block - 10]
        elif val_in_block < 100:
            # Handles tens like 20, 30, etc.
            if val_in_block % 10 == 0:
                return tens[val_in_block // 10]
            return tens[val_in_block // 10] + "-" + units[val_in_block % 10]
        else: # Numbers from 100 to 999
            hundreds_part = units[val_in_block // 100] + " hundred"
            remainder_part = val_in_block % 100
            if remainder_part == 0:
                return hundreds_part
            else:
                return hundreds_part + " " + process_block(remainder_part)

    # `word_segments` will store "one hundred", "two thousand", etc.
    word_segments = []
    # `magnitude_index` tracks if we're in thousands, millions, etc.
    magnitude_index = 0

    while number_val > 0:
        # Get the last three digits (a 'block' of numbers)
        current_block = number_val % 1000
        if current_block != 0:
            block_as_word = process_block(current_block)
            if magnitude_index > 0:
                word_segments.append(block_as_word + " " + magnitudes[magnitude_index])
            else:
                word_segments.append(block_as_word)
        number_val //= 1000
        magnitude_index += 1

    # `final_word_result` is the complete string
    final_word_result = " ".join(reversed(word_segments)).strip()
    if is_negative:
        return "negative " + final_word_result
    return final_word_result

if __name__ == "__main__":
    while True:
        try:
            user_input_string = input("Please enter a number (or 'quit' to exit): ")
            if user_input_string.lower() == 'quit':
                print("Exiting the program. Goodbye!")
                break
            parsed_number = int(user_input_string)
            words_output = convert_num_to_words(parsed_number)
            if words_output:
                print(f"The number {parsed_number} in words is: {words_output}")
            else:
                print("Could not convert that. Please enter a valid integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number or type 'quit'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")