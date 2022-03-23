import guess_game
import memory_game
import currency_roulette_game
from score import add_score

game_integer_to_play_function = {1: guess_game.play, 2: memory_game.play, 3: currency_roulette_game.play}

def welcome(name):
    return f"Hello {name} and welcome to the World of Games(WoG). Here you can find many cool games to play.\n"

def load_game():
    choose_game_prompt = """Please choose a game to play:
    * Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    * Guess Game - guess a number and see if you chose like the computer
    * Currency Roulette - try and guess the value of a random amount of USD in ILS
"""
    game_input = input(choose_game_prompt)
    choose_difficulty_prompt = "Please choose game difficulty from 1 to 5:\n"
    difficulty_input = input(choose_difficulty_prompt)

    is_game_input_valid = True
    if not game_input.isdigit():
        is_game_input_valid = False
    else:
        game_integer = int(game_input)
        if game_integer > 3 or game_integer < 1:
            is_game_input_valid = False

    is_difficulty_input_valid = True
    if not difficulty_input.isdigit():
        is_difficulty_input_valid = False
    else:
        difficulty_integer = int(difficulty_input)
        if difficulty_integer > 5 or difficulty_integer < 1:
            is_difficulty_input_valid = False

    if not is_game_input_valid:
        print("chosen game is not a valid number between 1 and 3")
    elif not is_difficulty_input_valid:
        print("chosen difficulty is not a valid number between 1 and 5")
    else:
        play_function = game_integer_to_play_function[game_integer]
        is_win = play_function(difficulty_integer)
        if is_win:
            add_score(difficulty_integer)
