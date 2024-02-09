# Task 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Task 2
def fahrenheit_to_centigrade(f):
    celsius = (5 / 9) * (f - 32)
    return celsius

# Task 3
def solve(num_heads, num_legs):
    rabbits = (num_legs - 2 * num_heads) / 2
    chickens = num_heads - rabbits
    return int(chickens), int(rabbits)

# Task 4
def filter_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return list(filter(lambda x: is_prime(x), nums))

# Task 5
from itertools import permutations

def string_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    return perms

# Task 6
def reverse_words(s):
    words = s.split()
    reversed_s = ' '.join(reversed(words))
    return reversed_s

# Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

# Task 9
def volume_of_sphere(radius):
    volume = (4 / 3) * 3.141592653589793 * (radius ** 3)
    return volume

# Task 10
def unique_elements_list(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Task 11
def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

# Task 12
def histogram(lst):
    for num in lst:
        print('*' * num)

# Task 13
import random

def guess_the_number_game():
    print("Hello! What is your name?")
    player_name = input()
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        player_guess = int(input())

        guesses_taken += 1

        if player_guess < secret_number:
            print("Your guess is too low.")
        elif player_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {guesses_taken} guesses!")
            break


