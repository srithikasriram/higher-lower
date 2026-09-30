import art
import game_data
import random


print(art.logo)

def select_a_celeb():
    """returns a randomly selected celeb from dictionary"""
    return game_data.data[random.randint(0, len(game_data.data)-1)]

def select_b_celeb():
    """returns a randomly selected celeb from dictionary that's not the same as celeb a"""
    b = game_data.data[random.randint(0, len(game_data.data) - 1)]
    while b == a_celeb:
        b = game_data.data[random.randint(0, len(game_data.data)-1)]
    return b

def print_celebs(celeb_one, celeb_two):
    """display celeb a and b's name, description, and country from dictionary data"""
    print(f"Compare A: {celeb_one['name']}, a {celeb_one['description']} from {celeb_one['country']}")
    print(art.vs)
    print(f"Against B: {celeb_two['name']}, a {celeb_two['description']} from {celeb_two['country']}\n")

def determine_winner(celeb_one, celeb_two, guess):
    """determine which celebrity has more followers"""
    if celeb_one['follower_count'] > celeb_two['follower_count']:
        if guess == "A":
            return True
        else:
            return False
    elif celeb_one['follower_count'] < celeb_two['follower_count']:
        if guess == "B":
            return True
        else:
            return False
    else:
        return False

a_celeb = select_a_celeb()
b_celeb = select_b_celeb()
score = 0

continue_game = True
while continue_game:
    print(art.logo)
    print_celebs(a_celeb, b_celeb)
    user_choice = str(input("Who do you think has more followers? Type 'A' or 'B': ")).upper()
    print("\n"*20)
    if determine_winner(a_celeb, b_celeb, user_choice):
        score+=1
        print(f"You're right! Current score: {score}")
        a_celeb = b_celeb
        b_celeb = select_b_celeb()
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry that's wrong. Final Score: {score}")
        continue_game = False


