import random
import time

def play(difficulty):
    generated = generate_sequence(difficulty)
    print("get ready to memorize the numbers...")
    time.sleep(2)
    print(generated, end="\r")
    time.sleep(0.7)
    print(" "*(difficulty*5+2))

    user_input = get_list_from_user()
    is_win = is_list_equal(user_input, generated)

    if is_win:
        print("You win.")
    else:
        print("You lose.")

    return is_win


def generate_sequence(difficulty):
    generated_list = []

    for _ in range(difficulty):
        generated_list.append(random.randint(1, 101))

    return generated_list

def get_list_from_user():
    input_ = input("Please enter the numbers you saw:")

    list_of_strings = input_.split(",")
    list_of_integers = [int(string.strip()) for string in list_of_strings]

    return list_of_integers

def is_list_equal(user_list, generated_list):
    if user_list == generated_list:
        return True
    else:
        return False