# author Arnaud Guilhamat guia2612
# date 2022-10-10

intercepted_message = 'fytgpcdtep op dspcmczzvp'

# Function that translates a character (Python code from question 1)
def translate(char, key):
    i = ord(char) - ord('a')
    i = (i + key) % 26
    return chr(i + ord('a'))


def encrypt(clear_text, key):
    clear_text = clear_text.lower()  # Convert to lower case
    cipher_text = ''

    for char in clear_text:
        if (ord(char) >= ord('a')) and (ord(char) <= ord('z')):
            cipher_text += translate(char, key)
        else:
            cipher_text += char

    return cipher_text


# The decrypt function is the same as the encrypt function, but with the opposite key number
def decrypt(cipher_text, key):
    key = -key
    clear_text = encrypt(cipher_text, key)
    return clear_text


def brute_force(intercepted_message):
    brute_force_dict = {}
    for key in range(26):
        brute_force_dict[key] = decrypt(intercepted_message, key)

    return brute_force_dict


# message = "HeLlo wOrld99*&*&*@"
# intercepted_message = 'khoor zruog99*&*&*@'
# key = 3 + 26

# print(encrypt(message, key))
# print(decrypt(message, key))
# print(decrypt(encrypt(message, key), key))

# print(brute_force(intercepted_message))
