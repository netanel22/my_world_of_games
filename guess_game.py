import random

def play(difficulty):
    generated = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    is_win = compare_results(guess, generated)

    if is_win:
        print("You win.")
    else:
        print("You lose.")

    return is_win

def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    guess_input = input("Please enter your guess:")

    is_guess_input_valid = True
    if not guess_input.isdigit():
        is_guess_input_valid = False
    else:
        guess_integer = int(guess_input)
        if guess_integer > difficulty or guess_integer < 1:
            is_guess_input_valid = False

    if not is_guess_input_valid:
        print(f"guess is not a valid number between 1 and {difficulty}")
        return None
    else:
        return guess_integer

def compare_results(guess, generated):
    if guess == generated:
        return True
    else:
        return False