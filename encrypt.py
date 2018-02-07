message = "This is a test, a TEST of all good things that come from encryption!"

encrypt_key = {'a': 'z', 'b': 'n', 'c': 'B', 'd': '%', 'e': '}', 'f': 'k', 'g': 'm', 'h': '3', 'i': 'G', 'j': 'j',
               'k': '[', 'l': '_', 'm': '7', 'n': 'J', 'o': 'W', 'p': 'q', 'q': 'L', 'r': 'Z', 's': 'c', 't': 'r',
               'u': 'Q', 'v': '.', 'w': 'o', 'x': 'l', 'y': 'K', 'z': 'P', 'A': 'b', 'B': 'U', 'C': 'v', 'D': '2',
               'E': 'w', 'F': '&', 'G': '9', 'H': 'x', 'I': '$', 'J': 'T', 'K': 'N', 'L': 'H', 'M': '#', 'N': '8',
               'O': '!', 'P': 'a', 'Q': 'y', 'R': '0', 'S': ',', 'T': 't', 'U': 'd', 'V': 'C', 'W': ']', 'X': '4',
               'Y': '1', 'Z': '6', ' ': '^', '.': 'e', ',': '|', '{': 'f', '}': '-', '!': '<', '@': '?', '#': 'Y',
               '$': 'E', '%': '@', '^': ' ', '&': '5', '*': 's', '?': '{', '-': 'X', '_': 'I', '<': 'A', '>': '>',
               '[': 'R', ']': 'D', '|': 'g', '0': '*', '1': 'V', '2': 'F', '3': 'i', '4': 'O', '5': 'M', '6': 'p',
               '7': 'S', '8': 'u', '9': 'h', }

decrypt_key = dict((v,k) for k, v in encrypt_key.items())


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
