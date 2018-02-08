from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
import random

punctuation = ' .,{}!@#$%^&*?-_<>[]|'

all_characters = ascii_lowercase + ascii_uppercase + punctuation + digits
total_char = len(all_characters)
used_characters = []

encrypt_key = {}


def get_random_char():
    index = random.randint(0, total_char - 1)
    random_char = all_characters[index]

    return random_char


for key in all_characters:
    temp_char = get_random_char()

    while temp_char in used_characters:
        temp_char = get_random_char()

    used_characters.append(temp_char)

    encrypt_key[key] = temp_char

print('encrypt_key = {', end="")
for key in encrypt_key:
    print('\'{}\': \'{}\','.format(key, encrypt_key[key]), end=" ")
print('}', end="")

print()
print('decrypt_key = {', end="")
for key in encrypt_key:
    print('\'{}\': \'{}\','.format(encrypt_key[key], key), end=" ")
print('}', end="")
