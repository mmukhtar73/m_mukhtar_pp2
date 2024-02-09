# Exercise 1
def g2o(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_value = float(input())
ounces_result = g2o(grams_value)
print(f"{grams_value} grams is equal to {ounces_result:.2f} ounces.")

# Exercise 2
def f2c(f):
    c = (5 / 9) * (f - 32)
    return c

f_temp = float(input())
c_result = f2c(f_temp)
print(f"{f_temp}°F is equal to {c_result:.2f}°C.")

# Exercise 3
def solve(heads, legs):
    rabbits = (legs - 2 * heads) / 2
    chickens = heads - rabbits
    return int(chickens), int(rabbits)

heads = 35
legs = 94
ch, rb = solve(heads, legs)
print(f"We have {ch} chickens and {rb} rabbits.")

# Exercise 4
def filter_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return list(filter(lambda x: is_prime(x), nums))

number_list = list(map(int, input().split()))
prime_numbers_result = filter_prime(number_list)
print("Prime Numbers:", prime_numbers_result)

# Exercise 5
from itertools import permutations

def string_perms(s):
    perms = [''.join(p) for p in permutations(s)]
    return perms

user_input_string = input()
perms_result = string_perms(user_input_string)
print("Permutations:", perms_result)

# Exercise 6
def reverse_sentence(s):
    words = s.split()
    reversed_s = ' '.join(reversed(words))
    return reversed_s

user_input_sentence = input()
reversed_result = reverse_sentence(user_input_sentence)
print("Reversed Sentence:", reversed_result)

# Exercise 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# Exercise 8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# Exercise 9
def vol_of_sphere(r):
    volume = (4 / 3) * 3.141592653589793 * (r ** 3)
    return volume

sphere_radius = float(input())
sphere_volume = vol_of_sphere(sphere_radius)
print(f"Volume of the sphere: {sphere_volume:.2f} cubic units.")

# Exercise 10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

numbers_list = list(map(int, input().split()))
unique_numbers_result = unique_elements(numbers_list)
print("Unique Numbers:", unique_numbers_result)

# Exercise 11
def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

user_input_word = input()
if is_palindrome(user_input_word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

# Exercise 12
def histogram(nums):
    for num in nums:
        print('*' * num)

histogram([4, 9, 7])

# Exercise 13
import random

def guess_game():
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
            print(f"Good job, {player_name}! You guessed the number in {guesses_taken} guesses.")
            break

guess_game()
