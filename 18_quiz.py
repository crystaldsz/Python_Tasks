# Simple Quiz App
# Create a console-based quiz app with questions and multiple-choice answers.

# ANSI escape codes for terminal colors. These are standard text formatting codes,
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
quiz_data = [
    {
        "q": "What is the capital of France?",
        "ops": ["London", "Berlin", "Paris", "Rome"],
        "ans": "Paris"
    },
    {
        "q": "Which planet is known as the 'Red Planet'?",
        "ops": ["Earth", "Mars", "Jupiter", "Venus"],
        "ans": "Mars"
    },
    {
        "q": "What is the largest ocean on Earth?",
        "ops": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "ans": "Pacific Ocean"
    },
    {
        "q": "What is the chemical symbol for water?",
        "ops": ["O2", "H2O", "CO2", "NACL"],
        "ans": "H2O"
    },
    {
        "q": "Who painted the Mona Lisa?",
        "ops": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "ans": "Leonardo da Vinci"
    }
]
_seed = 12345 
_multiplier = 1103515245
_increment = 12345
_modulus = 2**31 - 1

def get_rand_num(min_val, max_val):
    global _seed 
    _seed = (_multiplier * _seed + _increment) % _modulus
    return min_val + (_seed % (max_val - min_val + 1))

def shuffle_items(items):
    num_items = len(items)
    for i in range(num_items - 1, 0, -1):
        j = get_rand_num(0, i)
        temp = items[i]
        items[i] = items[j]
        items[j] = temp


def run_quiz():
    score = 0 

    shuffle_items(quiz_data) 
    print(f"{C_BOLD}{C_CYAN}Welcome to the Awesome Python Quiz!{C_RESET}")
    print(f"{C_YELLOW}Let's test your knowledge!{C_RESET}\n")

    for i, q_details in enumerate(quiz_data):
        print(f"{C_BOLD}{C_CYAN}--- Question {i+1} ---{C_RESET}")
        print(f"{C_CYAN}{q_details['q']}{C_RESET}")

        for j, option_text in enumerate(q_details['ops']):
            print(f"{C_YELLOW}{j+1}. {option_text}{C_RESET}")

        while True:
            try:
                # Ask the user to pick an option by number.
                user_ans_idx = int(input(f"{C_YELLOW}Enter the number of your answer: {C_RESET}")) - 1
                
                # Validate if the entered number corresponds to an actual option.
                if 0 <= user_ans_idx < len(q_details['ops']):
                    user_choice_text = q_details['ops'][user_ans_idx]
                    break
                else:
                    print(f"{C_RED}Invalid input. Please enter a number corresponding to an option.{C_RESET}")
            except ValueError: 
                print(f"{C_RED}Invalid input. Please enter a number.{C_RESET}")


        if user_choice_text == q_details['ans']:
            print(f"{C_GREEN}Correct! Well done!{C_RESET}\n")
            score += 1
        else:
            print(f"{C_RED}Incorrect! The correct answer was: {C_BOLD}{q_details['ans']}{C_RESET}\n")

    # After all questions, display the final score and a message.
    print(f"{C_BOLD}{C_CYAN}--- Quiz Finished! ---{C_RESET}")
    print(f"{C_BOLD}{C_GREEN}You scored {score} out of {len(quiz_data)} questions.{C_RESET}")
    
    if score == len(quiz_data):
        print(f"{C_BOLD}{C_GREEN}Congratulations! You got all of them right!{C_RESET}")
    elif score >= len(quiz_data) // 2: 
        print(f"{C_BOLD}{C_YELLOW}Good job! Keep learning!{C_RESET}")
    else:
        print(f"{C_BOLD}{C_RED}You can do better! Keep practicing!{C_RESET}")
        
if __name__ == "__main__":
    run_quiz()