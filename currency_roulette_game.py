import random
import json
from subprocess import check_output

def play(difficulty):
    random_number = random.randint(1, 100)

    usd_to_ils_exchange_rate = get_exchange_rate()

    random_number_in_ils = random_number * usd_to_ils_exchange_rate

    correct_interval = get_money_interval(random_number_in_ils, difficulty)

    guess = get_guess_from_user(random_number)

    is_win = compare_results(guess, correct_interval)

    if is_win:
        print("You win.")
    else:
        print("You lose.")

    return is_win

def get_exchange_rate():
    output = check_output(["curl", "-s", "https://freecurrencyapi.net/api/v2/latest?apikey=fdc72140-8161-11ec-8b22-01b88d31dd3a"])
    output_dictionary = json.loads(output)
    usd_to_ils_exchange_rate = output_dictionary["data"]["ILS"]

    return  usd_to_ils_exchange_rate

def get_money_interval(random_number, difficulty):
    start = random_number - (5 - difficulty)
    end = random_number + (5 - difficulty)
    return start, end

def get_guess_from_user(random_number):
    guess_input = input(f"Please enter your guess of ILS value of {random_number} USD:")

    is_guess_input_valid = True
    try:
        guess_float = float(guess_input)
    except ValueError:
        is_guess_input_valid = False

    if not is_guess_input_valid:
        print(f"guess is not a valid number")
        return None
    else:
        return guess_float

def compare_results(guess, correct_interval):
    if correct_interval[0] <= guess <= correct_interval[1]:
        return True
    else:
        return False
