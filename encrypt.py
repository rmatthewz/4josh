message = "This is a test, a TEST of all good things, the #1 good things, that come from encryption!"

encrypt_key = {'a': 'K', 'b': 'R', 'c': 'B', 'd': 'h', 'e': 'i', 'f': '!', 'g': 'b', 'h': 'V', 'i': 'y', 'j': 'p',
               'k': 'r', 'l': '7', 'm': '%', 'n': 'a', 'o': 'Y', 'p': 't', 'q': 'P', 'r': '[', 's': 'l', 't': 'v',
               'u': 'M', 'v': '*', 'w': ',', 'x': 'O', 'y': '0', 'z': '9', 'A': 'Q', 'B': 'A', 'C': 'S', 'D': 's',
               'E': '_', 'F': 'T', 'G': '}', 'H': 'E', 'I': 'o', 'J': '-', 'K': '5', 'L': 'W', 'M': '?', 'N': 'w',
               'O': 'D', 'P': 'k', 'Q': ']', 'R': 'j', 'S': 'F', 'T': 'x', 'U': 'I', 'V': 'f', 'W': '<', 'X': '2',
               'Y': '4', 'Z': '3', ' ': 'z', '.': '@', ',': 'u', '{': 'd', '}': '{', '!': '6', '@': '|', '#': '^',
               '$': 'Z', '%': 'J', '^': '>', '&': 'c', '*': '$', '?': 'L', '-': 'N', '_': '.', '<': '#', '>': ' ',
               '[': 'g', ']': '8', '|': 'X', '0': 'n', '1': 'm', '2': 'q', '3': 'G', '4': 'C', '5': 'H', '6': '1',
               '7': '&', '8': 'U', '9': 'e', }

decrypt_key = {'K': 'a', 'R': 'b', 'B': 'c', 'h': 'd', 'i': 'e', '!': 'f', 'b': 'g', 'V': 'h', 'y': 'i', 'p': 'j',
               'r': 'k', '7': 'l', '%': 'm', 'a': 'n', 'Y': 'o', 't': 'p', 'P': 'q', '[': 'r', 'l': 's', 'v': 't',
               'M': 'u', '*': 'v', ',': 'w', 'O': 'x', '0': 'y', '9': 'z', 'Q': 'A', 'A': 'B', 'S': 'C', 's': 'D',
               '_': 'E', 'T': 'F', '}': 'G', 'E': 'H', 'o': 'I', '-': 'J', '5': 'K', 'W': 'L', '?': 'M', 'w': 'N',
               'D': 'O', 'k': 'P', ']': 'Q', 'j': 'R', 'F': 'S', 'x': 'T', 'I': 'U', 'f': 'V', '<': 'W', '2': 'X',
               '4': 'Y', '3': 'Z', 'z': ' ', '@': '.', 'u': ',', 'd': '{', '{': '}', '6': '!', '|': '@', '^': '#',
               'Z': '$', 'J': '%', '>': '^', 'c': '&', '$': '*', 'L': '?', 'N': '-', '.': '_', '#': '<', ' ': '>',
               'g': '[', '8': ']', 'X': '|', 'n': '0', 'm': '1', 'q': '2', 'G': '3', 'C': '4', 'H': '5', '1': '6',
               '&': '7', 'U': '8', 'e': '9', }

# decrypt_key = dict((v,k) for k, v in encrypt_key.items())


def encrypt(a_message):
    encrypted = ''

    for letter in a_message:
        value = encrypt_key[letter]
        encrypted = encrypted + value

    return encrypted


def decrypt(a_message):
    decrypted = ''

    for letter in a_message:
        value = decrypt_key[letter]
        decrypted = decrypted + value

    return decrypted


print("Original message: " + message)
encrypted_message = encrypt(message)
print("Encrypted message: " + encrypted_message)
decrypted_message = decrypt(encrypted_message)
print("Decrypted message: " + decrypted_message)
