message = "This is a test, a TEST of all good things, the #1 good things, that come from encryption!"

encrypt_key = {'a': '7', 'b': 'n', 'c': 'o', 'd': ';', 'e': 'r', 'f': 'H', 'g': 'y', 'h': '0', 'i': 'l', 'j': ':',
               'k': 'J', 'l': '}', 'm': 'b', 'n': '<', 'o': '3', 'p': 'P', 'q': 'B', 'r': '%', 's': '*', 't': 'U',
               'u': '|', 'v': '6', 'w': 'X', 'x': 'I', 'y': 'u', 'z': 'G', 'A': '>', 'B': 's', 'C': 'C', 'D': '4',
               'E': '8', 'F': 'x', 'G': 'h', 'H': 't', 'I': 'E', 'J': '~', 'K': '@', 'L': '$', 'M': 'R', 'N': '.',
               'O': 'K', 'P': 'v', 'Q': 'M', 'R': 'F', 'S': 'm', 'T': 'e', 'U': 'O', 'V': 'q', 'W': '#', 'X': '5',
               'Y': 'T', 'Z': 'k', ' ': '?', '.': '-', ',': 'S', '{': 'Y', '}': 'z', '!': 'N', '@': 'L', '#': 'i',
               '$': 'g', '%': '!', '^': 'D', '&': 'j', '*': ' ', '?': 'd', '-': 'V', '_': 'p', '<': '2', '>': '+',
               '[': '_', ']': '{', '|': 'Q', ':': '1', ';': '[', '~': 'c', '+': ',', '0': 'w', '1': 'a', '2': 'A',
               '3': '^', '4': '9', '5': '&', '6': 'Z', '7': ']', '8': 'W', '9': 'f', }

decrypt_key = {'7': 'a', 'n': 'b', 'o': 'c', ';': 'd', 'r': 'e', 'H': 'f', 'y': 'g', '0': 'h', 'l': 'i', ':': 'j',
               'J': 'k', '}': 'l', 'b': 'm', '<': 'n', '3': 'o', 'P': 'p', 'B': 'q', '%': 'r', '*': 's', 'U': 't',
               '|': 'u', '6': 'v', 'X': 'w', 'I': 'x', 'u': 'y', 'G': 'z', '>': 'A', 's': 'B', 'C': 'C', '4': 'D',
               '8': 'E', 'x': 'F', 'h': 'G', 't': 'H', 'E': 'I', '~': 'J', '@': 'K', '$': 'L', 'R': 'M', '.': 'N',
               'K': 'O', 'v': 'P', 'M': 'Q', 'F': 'R', 'm': 'S', 'e': 'T', 'O': 'U', 'q': 'V', '#': 'W', '5': 'X',
               'T': 'Y', 'k': 'Z', '?': ' ', '-': '.', 'S': ',', 'Y': '{', 'z': '}', 'N': '!', 'L': '@', 'i': '#',
               'g': '$', '!': '%', 'D': '^', 'j': '&', ' ': '*', 'd': '?', 'V': '-', 'p': '_', '2': '<', '+': '>',
               '_': '[', '{': ']', 'Q': '|', '1': ':', '[': ';', 'c': '~', ',': '+', 'w': '0', 'a': '1', 'A': '2',
               '^': '3', '9': '4', '&': '5', 'Z': '6', ']': '7', 'W': '8', 'f': '9', }


# decrypt_key = dict((v,k) for k, v in encrypt_key.items())


def encrypt(a_message):
    encrypted = ''

    for letter in a_message:
        value = encrypt_key[letter]
        encrypted = encrypted + value

    cipher_text = pad_string(encrypted)

    return cipher_text


def pad_string(string):
    return_string = ''

    for index in range(0, len(string) - 1):
        return_string += string[index]
        if (index + 1) % 5 == 0:
            return_string += ' '

    return return_string


def decrypt(a_message):
    decrypted = ''

    for letter in a_message:
        if letter != ' ':
            value = decrypt_key[letter]
            decrypted = decrypted + value

    return decrypted


print("Original message: " + message)
encrypted_message = encrypt(message)
print("Encrypted message: " + encrypted_message)
decrypted_message = decrypt(encrypted_message)
print("Decrypted message: " + decrypted_message)
